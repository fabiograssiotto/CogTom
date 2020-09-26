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

    def set(self, max_steps):
        self.logger = Logger(Logger.MODULES_MEMORY, max_steps)                                
    
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

            # Loop through each row of the update dataframe, to check if the
            # memory content should be updated.
            drop_list = []
            for index, entry in df.iterrows():
                if (entry['Target_Obj'] == 'None'):
                    # No Target Obj, probably there was no intention associated 
                    # to the Agent/Object pair.
                    # Check if the memory already has a belief associated.
                    agt = entry['Agent']
                    obj = entry['Object']
                    
                    try:
                        findRow = self.belief_df.loc[agt, obj]
                    except KeyError:
                        # Does not exist in Dataframe, keep going.
                        continue

                    if (findRow['Target_Obj'] != 'None'):
                        # add to drop list, since we have a belief resulting from an intention.
                        drop_list.append(index)
            df = df.drop(drop_list)

            # Update the remaining rows.
            self.belief_df.update(df)
            self.belief_df = self.belief_df.combine_first(df)

    def get_people(self):
        # Returns the set of the agents in the environment
        agents = set(self.belief_df['Agent'].unique())
        agents.remove('Observer')
        return agents

    def get_things(self):
        agents = self.get_people()
        # set of objects
        objects = set(self.belief_df['Object'].unique()) - agents
        # Remove agents from objects list.
        return objects

    def get_person_beliefs(self, person):
        df = self.belief_df[self.belief_df['Agent'] == person]
        return df
    
    def get_thing_beliefs(self, object):
        df = self.belief_df[self.belief_df['Object'] == object]
        return df

    def get_observer_beliefs(self):
        df = self.belief_df[self.belief_df['Agent'] == 'Observer']
        return df

    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg, t)
        self.logger.write("Belief Memory: ", t)
        self.logger.write(self.belief_df.reset_index(drop = True).to_string(), t)
