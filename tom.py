# Theory of Mind Module
#
# 
import numpy as np

class ToM:

    # The set of mental states ToM represents.
    MENTAL_STATES = ["SEES", "BELIEVES"]

    def __init__(self, affordances, id, edd, sam):
        self.afford = affordances.values.tolist() # List of affordances for the objects in the environment
        self.id = id
        self.edd = edd
        self.sam = sam
        self.goals = id.goals()
        self.tom_beliefs = []

    def process(self):
        # Create representations of the mental states 
        # of the form Agent-Mental State-Object

        #'SEES' mental state.
        for agent in range(self.edd.edd_eyes.shape[0]):
            tom_belief = []
            # For each agent line in edd_eyes
            # Retrieve the list of objects the agent sees.
            tom_belief.append(self.edd.edd_eyes[agent])
            tom_belief.append(self.MENTAL_STATES[0])
            for ent in range(self.edd.edd_agent_store.shape[1]):
                tom_belief.append(self.edd.edd_agent_store[agent][ent])
                self.tom_beliefs.append(tom_belief.copy())
                del tom_belief[-1]

        #'BELIEVES' mental state
        

    def print(self):
        print("ToM:")
        print("Agents: ", self.id.agents())
        print("Beliefs: ", self.tom_beliefs)
        print("\n")