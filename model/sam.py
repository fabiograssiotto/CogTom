# Shared Attention Mechanism
# SAM's function is to build "triadic representations" 
# to compute if two agents are seeing the same thing.
# SAM relies on EDD information to build its internal representations.
import numpy as np

from model.edd import Edd

class Sam:

    def __init__(self, edd):
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

    def print(self, logger):
        logger.write("SAM:")
        logger.write("Entities on scene: " + str(self.entities))
        logger.write("Agents on scene: " + str(self.agents))
        logger.write("Agents with shared attention: " + str(self.shared_attn_list))
