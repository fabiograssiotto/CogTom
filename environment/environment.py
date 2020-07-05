# Environment
# Manages the inputs from the environment, simulating 
# visual and mind inputs.
import pandas as pd
import os
import numpy as np

class Environment:

    def __init__(self):
        # List of scenes the system can analyse.
        folder = "scenes"
        self.folders = [f.name for f in os.scandir(folder) if f.is_dir()]

    def get_scenes(self):
        return self.folders
    
    def set_scene(self, scene):

        folder = 'scenes/' + scene + '/'

        # Textual descriptions for each scene
        self.scene_df = pd.read_csv(folder + 'scenes.txt',
                                    sep = ':',
                                    comment = '#')

        # Identifying entities (agents and objects) in the scene.
        self.entities_df = pd.read_csv(folder + 'entities.txt',
                                        delim_whitespace=True,
                                        comment='#')

        # Eye Direction System, identifies which entities are in the visual field of an agent.
        self.eye_dir_df = pd.read_csv(folder + 'eye_directions.txt',
                                       delim_whitespace=True,
                                       comment='#')

        # Intention Detection System, identifies intentions for the agents in the visual field.
        self.intention_df = pd.read_csv(folder + 'intentions.txt',
                                         delim_whitespace=True,
                                         comment='#')

        # Affordances, or properties, for the objects in the scene.
        self.afford_df = pd.read_csv(folder + 'affordances.txt',
                                      delim_whitespace=True,
                                      comment='#')
        self.time_step = 1

    def set_time_step(self, t):
        # Sets the current time step.
        # Returns -1 if the environment indicates the end of the simulation.
        self.time_step = t
        self.scene_info = self.scene_df.loc[self.scene_df['t'] == t]
        self.entities_info = self.entities_df.loc[self.entities_df['t'] == t]
        self.eye_dir_info = self.eye_dir_df.loc[self.eye_dir_df['t'] == t]
        self.intention_info = self.intention_df.loc[self.intention_df['t'] == t]
        if (self.entities_info.empty == True):
            # Empty dataframe, so there are no more simulation steps.
            return -1
        else:
            self.scene_info = self.scene_info.drop(columns='t')
            self.entities_info = self.entities_info.drop(columns='t')
            self.eye_dir_info = self.eye_dir_info.drop(columns='t')
            self.intention_info = self.intention_info.drop(columns='t')
            return 0

    def get_max_time_step(self):
        return self.entities_df['t'].max()

    def get_scene(self):
        return str(self.scene_info['Scene'].values[0])

    def get_agents(self):
        # Returns a list of the agents in the current time step.
        agents = self.entities_info.loc[self.entities_info['Is_Agent'] == True]
        return agents['Entity'].tolist()
        
    def get_entities(self):
        # Entities combine Agents and Objects
        entities_arr = np.array(self.entities_info['Entity'].tolist())
        is_agent_arr = np.array(self.entities_info['Is_Agent'].tolist())
        return np.column_stack((entities_arr, is_agent_arr))
    
    def get_eye_dir(self):
        # Do the same operation to the eye direction information
        # for the current time step.
        return self.eye_dir_info.to_numpy()

    def get_affordances(self):
        return self.afford_df.values.tolist()
    
    def get_intentions(self):
        intentions = self.intention_info.loc[self.intention_info['Intention'] != 'None']
        return intentions[['Agent', 'Intention', 'Object', 'Target']].values.tolist()

    def get_time_step(self):
        return self.time_step
