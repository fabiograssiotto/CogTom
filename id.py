# Id Class
# Holds a list of all the agents in a scene.
class Id:
    def __init__(self, entities):
        agents = entities.loc[entities['Animated'] == True]
        self.Id_Agent = agents['Entity'].tolist()

    def agents():
        return Id_Agent
    
    def print(self):
        # Basic debugging
        print("Agents: ", *self.Id_Agent)
        
