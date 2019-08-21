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
    
    def print(self):
        # Basic debugging
        print("EDD_entities: ", self.edd_entities[:,0])
        print("EDD_Eye_Direction: \n", self.edd_eye_dir)
        print()





        

        


