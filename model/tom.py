# Theory of Mind Module
# ToM represents mental states
# described as triads of form Agent-Mental State-Object
import numpy as np
from output.logger import Logger
from model.model import Model

class ToM:

    # The set of mental states ToM represents.
    # Lets start with the BELIEF mental state.
    MENTAL_STATES = ["Believes"]

    def __init__(self):
        Model.__init__(self, Logger.MODEL_TOM)

    def set(self, affordances,intentions, id, edd, sam, mem):
        self.afford = affordances
        self.intentions = intentions
        self.id = id
        self.agents = id.agents
        self.edd = edd
        self.sam = sam
        self.memory  = mem
        self.tom_beliefs = []

    def process(self):
        # Create representations of the mental states 
        # of the form Agent-Mental State-Object

        # 'Believes' mental state
        # The mental state modeled here produces descriptions in the form
        # AGENT BELIEVES OBJECT AFFORDANCE or
        # AGENT BELIEVES OBJECT AFFORDANCE TARGET_OBJECT (due to a Drive)
        for agent in range(self.edd.edd_eyes.shape[0]):
            tom_belief = []
            # For each agent line in edd_eyes
            # Retrieve the list of objects the agent sees.
            tom_belief.append(self.edd.edd_eyes[agent])
            tom_belief.append(self.MENTAL_STATES[0])
            for ent in range(self.edd.edd_agent_store.shape[1]):
                obj = self.edd.edd_agent_store[agent][ent]
                tom_belief.append(obj)
                for sublist in self.afford:
                    if sublist[0] == obj:
                        # Object has an affordance.
                        tom_belief.append(sublist[1])
                        break
                # Check if intentions from the environment 
                # are likely to change beliefs.
                tom_belief = self.check_intentions(tom_belief)
                self.tom_beliefs.append(tom_belief.copy())
                del tom_belief[2:] # Only keeps Agent and Belief 

            # Add the list of beliefs at the end to the Belief Memory.
            self.memory.add(self.tom_beliefs)
        
    def check_intentions(self, belief):
        # Next step is to analyse INTENTIONS and verify Beliefs that could be 
        # modified based on intentions detected in the environment.
        for intention in self.intentions:
            agt = intention[0]
            intent = intention[1]
            obj = intention[2]
            tgt = intention[3]

            belief = self.map_intention(intent, obj, tgt, belief)

        if (len(belief) == 4):
            # Belief does not have a target object, set as None.
            belief.append('None')

        return belief

    def map_intention(self, intent, obj, tgt, belief):
        mapper = {
            'None': self.skip,
            'ReachFor': self.reachFor,
            'Puts': self.put,
            'Gets': self.get,
            'Exits': self.exit,
            'Enters': self.enter,
            'Search': self.search
        }
        # Get the function from mapper dictionary
        func = mapper.get(intent)
        # Execute the function
        return func(obj, tgt, belief)

    def skip(self, obj, tgt, belief):
        # Nothing to do
        return belief

    def reachFor(self, obj, tgt, belief):
        return belief
    
    def put(self, obj, tgt, belief):
        return belief

    def get(self, obj, tgt, belief):
        return belief
    
    def exit(self, obj, tgt, belief):
        return belief

    def enter(self, obj, tgt, belief):
        return belief

    def search(self, obj, tgt, belief):
        return belief
    

    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg)
        self.logger.write("ToM:")
        self.logger.write("Agents: " + str(self.agents()))
        self.logger.write("Intentions: " + str(self.intentions))
        self.logger.write("Beliefs: " + str(self.tom_beliefs))