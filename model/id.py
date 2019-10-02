# Intentionality Detector
# ID function has two functions:
#  - interprets motion stimuli to identify agents.
#  - identifies drives for each agent.
from output.logger import Logger
from model.model import Model

class Id(Model):
    def __init__(self):
        Model.__init__(self, Logger.MODEL_ID)

    def set(self, agents, drives):
        self.id_agents = agents
        self.id_drives = drives

    def agents(self):
        return self.id_agents

    def drives(self):
        return self.id_drives
    
    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg)
        # Output ID information
        self.logger.write("ID:")
        self.logger.write("Agents: " + str(self.id_agents))
        self.logger.write("Drives: " + str(self.id_drives))