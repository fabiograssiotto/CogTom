# Intentionality Detector
# ID function has two functions:
#  - interprets motion stimuli to identify agents.
#  - identifies drives for each agent.
class Id:
    def __init__(self, agents, drives):
        self.id_agents = agents
        self.id_drives = drives

    def agents(self):
        return self.id_agents

    def drives(self):
        return self.id_drives
    
    def print(self, logger):
        # Output ID information
        logger.write("ID:")
        logger.write("Agents: " + str(self.id_agents))
        logger.write("Drives: " + str(self.id_drives))