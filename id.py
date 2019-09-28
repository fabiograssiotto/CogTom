# Intentionality Detector
# ID function has two functions:
#  - interprets motion stimuli to identify agents.
#  - identifies drives for each agent.
class Id:
    def __init__(self, entities):
        agents = entities.loc[entities['Is_Moving'] == True]
        drives = entities.loc[entities['Drive'] != 'None']
        self.id_agents = agents['Entity'].tolist()
        self.id_drives = drives[['Entity', 'Drive', 'Drive-Object', 'Drive-Target']].values.tolist()

    def agents(self):
        return self.id_agents

    def drives(self):
        return self.id_drives
    
    def print(self):
        # Basic debugging
        print("ID:")
        print("Agents: ", self.id_agents)
        print("Drives: ", self.id_drives)
        print()
        
