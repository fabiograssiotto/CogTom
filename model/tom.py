# Theory of Mind Module
# ToM represents mental states
# described as triads of form Agent-Mental State-Object
import numpy as np

class ToM:

    # The set of mental states ToM represents.
    # Lets start with the BELIEF mental state.
    MENTAL_STATES = ["Believes"]

    def __init__(self, affordances, id, edd, sam, mem):
        self.afford = affordances
        self.id = id
        self.agents = id.agents
        self.drives = id.drives()
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
                # Check if drives from the environment 
                # are likely to change beliefs.
                tom_belief = self.check_drive(tom_belief)
                self.tom_beliefs.append(tom_belief.copy())
                del tom_belief[2:] # Only keeps Agent and Belief 

            # Add the list of beliefs at the end to the Belief Memory.
            self.memory.add(self.tom_beliefs)
        
    def check_drive(self, belief):
        # Next step is to analyse DRIVES and verify Beliefs that involve the drives in
        # the current mind step.
        for drv in self.drives:
            drive = drv[1]
            drive_obj = drv[2]
            drive_tgt = drv[3]

            # Check if this belief is modified by the at least one of the drives.
            if belief[2] == drive_obj:
                if (drive == 'Hide'):
                    belief[3] = 'Hidden in'
                    belief.append(drive_tgt)
                    break
                elif (drive == 'Get'):
                    # TODO
                    break
                elif (drive == 'Search'):
                    # TODO
                    break
        if (len(belief) == 4):
            # Belief does not have a target object, set as None.
            belief.append('None')

        return belief

    def print(self, logger):
        logger.write("ToM:")
        logger.write("Agents: ", self.agents())
        logger.write("Drives: ", self.drives)
        logger.write("Beliefs: ", self.tom_beliefs)
        logger.write("")