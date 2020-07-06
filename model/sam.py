# Shared Attention Mechanism
# SAM's function is to build "triadic representations" 
# to compute if two agents are seeing the same thing.
# SAM relies on EDD information to build its internal representations.
import numpy as np
import pandas as pd

from .edd import Edd
from .model import Model
from output.logger import Logger

class Sam(Model):

    def __init__(self, max_steps):
        Model.__init__(self, Logger.MODEL_SAM, max_steps)
        
    def set(self, edd):
        self.edd = edd
        self.entities = [] # List of entities on the scene
        self.agents = [] # List of agents on the scene
        self.shared_attn_list = [] # List of lists with shared attention agents for each entity in the scene.

    def process(self):
        # SAM will try to identify, for each entity in the scene,
        # if any two agents are paying attention to it, using EDD structures.

        self.entities = self.edd.edd_entities[:,0].tolist()
        self.agents = self.edd.edd_eyes.tolist()

        for ent in self.entities:
            # For each entity in the list of entities
            # Find if there are at least two agents paying attention to it,
            # and record this.
            col = self.entities.index(ent) # Gets position in list, to access the column in EDD_Eye_Direction
            sam_lst = self.edd.edd_eye_dir[:,col].tolist()
            sam_idx_lst = [idx for idx, val in enumerate(sam_lst) if val == 1]
            if len(sam_idx_lst) >= 2:
                # found at least 2 agents paying attention.
                shared_attn = []
                shared_attn.append(ent)
                for ag_idx in sam_idx_lst:
                    shared_attn.append(self.agents[ag_idx])
                self.shared_attn_list.append(shared_attn)

    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg, t)
        self.logger.write("SAM:", t)
        self.logger.write("Entities on scene: " + str(self.entities), t)
        self.logger.write("Agents on scene: " + str(self.agents), t)
        self.logger.write("Agents with shared attention: " + str(self.shared_attn_list), t)

        # Latex
        df_shared_attn = pd.DataFrame(self.shared_attn_list, columns = ['Object', 'Agent 1', 'Agent 2'])
        if not df_shared_attn.empty:
            self.logger.write_tex(df_shared_attn.to_latex(index=False, caption='SAM Shared Attention Table'), t)
