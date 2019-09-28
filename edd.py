# Eye-Direction Detector
# EDD basic functions are:
#   detects the presence of eyes/eyes-like stimuli
#   computes whether eyes are directed towards agents/objects
#   infers agents knowledge attributing perceptual states.
import numpy as np

class Edd:

    def __init__(self, entities, agents):
        entities_arr = np.array(entities['Entity'].tolist())
        is_agent_arr = np.array(entities['Is_Moving'].tolist())

        self.edd_entities = np.column_stack((entities_arr, is_agent_arr))
        # Assume that all agents have eyes.
        self.edd_eyes = np.array(agents)

    def process(self, eye_dir):
        # Dimensions for the EDD Eye Direction Array are (agent) lines
        # and (entities) columns.
        lines = self.edd_eyes.shape[0]
        cols = self.edd_entities.shape[0] 

        self.edd_eye_dir = np.zeros((lines, cols), dtype=int)
        # Fill in Eye Direction Array based on the visual system.
        eye_dir_arr = eye_dir.to_numpy()
        for entry in range(eye_dir_arr.shape[0]):
            # For each line in the visual system, identify the object 
            # and fill in the EDD eye direction array.
            # By convention the array is configured as:
            #         Agent1 Obj1 Obj2 Obj3
            # Agent1     0    0/1  0/1  0/1
            # Agent2     0    0/1  0/1  0/1
            # where 0 is no gaze and 1 is a gaze.
            agent = eye_dir_arr[entry, 0]
            obj = eye_dir_arr[entry, 1]
            # identify row for insertion
            l = np.where(self.edd_eyes == agent)[0]
            c =  np.where(self.edd_entities == obj)[0]
            # Set as '1' to identify a object that is in the visual field of the agent.
            self.edd_eye_dir[l, c] = 1

        # Now create the EDD Agent store
        # For each agent list the entities in its visual space
        self.edd_agent_store = np.array([])
        ag_store_lst = []
        for agent in range(self.edd_eyes.shape[0]):
            # For each agent line in edd_eyes
            ag_list = []
            for eye_dir in range(self.edd_eye_dir.shape[1]):
                if self.edd_eye_dir[agent, eye_dir] == 1:
                    # Add to agent store
                    ag_list.append(self.edd_entities[eye_dir,0])
            ag_store_lst.append(ag_list)
        self.edd_agent_store = np.array(ag_store_lst)
        
        # Create EDD Gaze Register
        # The Gaze Register identifies agents that are looking at each other.
        mg_lst = []
        for ag in range(self.edd_eyes.shape[0]):
            # For each agent line in edd_eyes
            agent1 = self.edd_eyes[ag]
            for eye_dir in range(self.edd_eye_dir.shape[1]):
                if self.edd_eye_dir[ag, eye_dir] == 1:
                    # Check if entity being looked at is an agent, too.
                    entity = self.edd_entities[eye_dir,0]
                    is_agent = self.edd_entities[eye_dir,1]
                    if (is_agent):
                        # It is an agent too, so check if it is also looking back at the first agent. 
                        # To do that, we search on the EDD eye direction matrix.
                        l = np.where(self.edd_eyes == entity)[0]
                        c = np.where(self.edd_entities == agent1)[0]
                        if self.edd_eye_dir[l,c] == 1:
                            # Mutual Gaze confirmed, add to list.
                            mg_tuple = (agent1, entity)
                            # Is it in the list, already? Check for duplicates.
                            mg_tuple_inv = mg_tuple[::-1]
                            if (mg_tuple not in mg_lst) and (mg_tuple_inv not in mg_lst):
                                mg_lst.append(mg_tuple)
        # Add list to np array.
        self.edd_gaze_register = np.array(mg_lst)
    
    def print(self):
        print("EDD:")
        print("Entities: ", self.edd_entities[:,0])
        print("Eye_Direction: ", self.edd_eye_dir)
        print("Agent_Store: ", self.edd_agent_store)
        print("Gaze_Register:", self.edd_gaze_register)
        print()





        

        


