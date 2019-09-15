# Intentionality Detector
# ID function is to interprets motion stimuli to identify agents.
class Id:
    def __init__(self, entities):
        agents = entities.loc[entities['Is_Moving'] == True]
        goals = entities.loc[entities['Goal'] != 'None']
        self.id_agents = agents['Entity'].tolist()
        self.id_goals = goals[['Entity', 'Goal', 'Goal-Object', 'Goal-Target']].values.tolist()

    def agents(self):
        return self.id_agents

    def goals(self):
        return self.id_goals
    
    def print(self):
        # Basic debugging
        print("ID:")
        print("Agents: ", self.id_agents)
        print("Goals: ", self.id_goals)
        print()
        
