# Belief Memory
# Memory for False Beliefs as registered by the ToM module.
# Allows the system to preserve beliefs between mind cycles.
import pandas as pd
from output.logger import Logger

class BeliefMemory:

    def __init__(self):
        # Create dataframe for Belief Memory
        self.belief_df = pd.DataFrame(columns = ['Agent', 'Belief', 'Object',
                                                 'Affordance', 'Target_Obj'])
        self.belief_df.set_index(['Agent','Object'], drop = False, inplace = True)
        self.logger = Logger(Logger.MODULES_MEMORY)                                
    
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

    def get_people(self):
        # Returns the set of the agents in the environment
        return set(self.belief_df['Agent'].unique())

    def get_objects(self):
        agents = self.get_people()
        # set of objects
        objects = set(self.belief_df['Object'].unique()) - agents
        # Remove agents from objects list.
        return objects

    def get_person_beliefs(self, person):
        df = self.belief_df[self.belief_df['Agent'] == person]
        return df
    
    def get_object_beliefs(self, object):
        df = self.belief_df[self.belief_df['Object'] == object]
        return df

    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg)
        self.logger.write("Belief Memory: ")
        self.logger.write(self.belief_df.reset_index(drop = True).to_string())
