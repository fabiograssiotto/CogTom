# Intentionality Detector
# ID function is to interprets motion stimuli to identify agents.
class Id:
    def __init__(self, entities):
        agents = entities.loc[entities['Is_Moving'] == True]
        self.Id_Agent = agents['Entity'].tolist()

    def agents(self):
        return self.Id_Agent
    
    def print(self):
        # Basic debugging
        print("Agents: ", *self.Id_Agent)
        
