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

        edd_entities = np.column_stack((entities_arr, is_agent_arr))
        # Assume that all agents have eyes.
        edd_eyes = np.array(agents)
