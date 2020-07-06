# Intentionality Detector
# ID function has two functions:
#  - interprets motion stimuli to identify agents.
#  - identifies drives for each agent.
from output.logger import Logger
from model.model import Model
import pandas as pd

class Id(Model):
    def __init__(self, max_steps):
        Model.__init__(self, Logger.MODEL_ID, max_steps)

    def set(self, agents):
        self.id_agents = agents

    def agents(self):
        return self.id_agents
    
    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg, t)
        # Output ID information
        self.logger.write("ID:", t)
        self.logger.write("Agents: " + str(self.id_agents), t)

        # Latex
        df_agt = pd.DataFrame(self.id_agents, columns=['Agents'])
        if not df_agt.empty:
            self.logger.write_tex(df_agt.to_latex(index=False, caption='ID Agents Table'), t)
