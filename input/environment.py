# Environment
# Manages the inputs from the environment, simulating 
# visual and mind inputs.
import pandas as pd
import numpy as np

class Environment:

    def __init__(self):
        # Basic input for scene. Start by accessing the camera input and identifying entities
        # in the scene.
        self.visual_df = pd.read_csv('input/visual.txt',
                                     delim_whitespace=True,
                                     comment='#')

        # Eye Direction System, identifies which entities are in the visual field of an agent.
        self.eye_dir_df = pd.read_csv('input/eye_direction.txt',
                                      delim_whitespace=True,
                                      comment='#')

        # Intention Detection System, identifies intentions for the agents in the visual field.
        self.intention_df = pd.read_csv('input/intentions.txt',
                                        delim_whitespace=True,
                                        comment='#')

        # Affordances, or properties, for the objects in the scene.
        self.afford_df = pd.read_csv('input/affordances.txt',
                                     delim_whitespace=True,
                                     comment='#')
        self.time_step = 1

    def set_time_step(self, t):
        # Sets the current time step.
        # Returns -1 if the environment indicates the end of the simulation.
        self.visual_info = self.visual_df.loc[self.visual_df['t'] == t]
        self.eye_dir_info = self.eye_dir_df.loc[self.eye_dir_df['t'] == t]
        self.intention_info = self.intention_df.loc[self.intention_df['t'] == t]
        if (self.visual_info.empty == True):
            # Empty dataframe, so there are no more simulation steps.
            return -1
        else:
            self.visual_info = self.visual_info.drop(columns='t')
            self.eye_dir_info = self.eye_dir_info.drop(columns='t')
            self.intention_info = self.intention_info.drop(columns='t')
            return 0

    def get_max_time_step(self):
        return self.visual_df['t'].max()

    def get_agents(self):
        # Returns a list of the agents in the current time step.
        agents = self.visual_info.loc[self.visual_info['Is_Moving'] == True]
        return agents['Entity'].tolist()

    def get_drives(self):
        drives = self.visual_info.loc[self.visual_info['Drive'] != 'None']
        return drives[['Entity', 'Drive', 'Drive-Object', 'Drive-Target']].values.tolist()
        
    def get_entities(self):
        # Entities combine Agents and Objects
        entities_arr = np.array(self.visual_info['Entity'].tolist())
        is_agent_arr = np.array(self.visual_info['Is_Moving'].tolist())
        return np.column_stack((entities_arr, is_agent_arr))
    
    def get_eye_dir(self):
        # Do the same operation to the eye direction information
        # for the current time step.
        return self.eye_dir_info.to_numpy()

    def get_affordances(self):
        return self.afford_df.values.tolist()
    
    def get_intentions(self):
        intentions = self.intention_info.loc[self.intention_info['Intention'] != 'None']
        return intentions[['Agent', 'Intention']].values.tolist()
