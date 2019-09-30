# Belief Memory
# Memory for False Beliefs as registered by the ToM module.
# Allows the system to preserve beliefs between mind cycles.
import pandas as pd

class BeliefMemory:

    def __init__(self):
        # Create dataframe for Belief Memory
        self.belief_df = pd.DataFrame(columns = ['Agent', 'Belief', 'Object',
                                                 'Affordance', 'Target_Obj'])
        self.belief_df.set_index(['Agent','Object'], drop = False, inplace = True)                                         
    
    def add(self, beliefs):
        # Adds the set of beliefs to the memory.
        # Memory beliefs already present are updated, not added again.
        df = pd.DataFrame(beliefs, columns = ['Agent', 'Belief', 'Object',
                                                 'Affordance', 'Target_Obj'])
        df.set_index(['Agent','Object'], drop = False, inplace = True)

        if (self.belief_df.empty):
            # Add all beliefs, this is the 1st mind cycle
            self.belief_df = self.belief_df.append(df)
        else:
            # Update and Add new ones as necessary.
            self.belief_df.update(df)
            self.belief_df = self.belief_df.combine_first(df)

    def print(self):
        print("Belief Memory: ")
        print(self.belief_df)
