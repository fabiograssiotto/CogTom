# Theory of Mind Module
# ToM represents mental states
# described as triads of form Agent-Mental State-Object
import numpy as np
import pandas as pd

from output.logger import Logger
from memory.affordancehandler import AffordanceHandler
from memory.intentionhandler import IntentionHandler
from .model import Model

class ToM(Model):

    # The set of mental states ToM represents.
    # Lets start with the BELIEF mental state.
    MENTAL_STATES = ["Believes"]

    def __init__(self, max_steps):
        Model.__init__(self, Logger.MODEL_TOM, max_steps)

    def set(self, affordances,intentions, id, edd, sam, mem):
        self.affordhdlr = AffordanceHandler(affordances)
        self.inthdlr = IntentionHandler(intentions)
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
        # AGENT BELIEVES OBJECT AFFORDANCE TARGET_OBJECT (due to an intention)
        for agent in range(self.edd.edd_eyes.shape[0]):
            tom_belief = []
            # For each agent line in edd_eyes
            # Retrieve the list of objects the agent sees.
            tom_belief.append(self.edd.edd_eyes[agent])
            tom_belief.append(self.MENTAL_STATES[0])
            for ent in range(self.edd.edd_agent_store.shape[1]):
                obj = self.edd.edd_agent_store[agent][ent]
                tom_belief.append(obj)
                
                # Check any affordances the entities may have.
                tom_belief = self.affordhdlr.check_affordances(tom_belief)

                # Check if intentions from the environment 
                # are likely to change beliefs.
                tom_belief = self.inthdlr.check_intentions(tom_belief)
                self.tom_beliefs.append(tom_belief.copy())
                del tom_belief[2:] # Only keeps Agent and Belief 

            # Add the list of beliefs at the end to the Belief Memory.
            self.memory.add(self.tom_beliefs)

    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg, t)
        self.logger.write("ToM:", t)
        self.logger.write("Agents: " + str(self.agents()), t)
        self.logger.write("Intentions: " + str(self.inthdlr.getintentions()), t)
        self.logger.write("Beliefs: " + str(self.tom_beliefs), t)

        # Latex
        df_intentions = pd.DataFrame(self.inthdlr.getintentions(), columns = ['Agent', 'Intention', 'Object','Target'])
        if not df_intentions.empty:
            self.logger.write_tex(df_intentions.to_latex(index=False, caption='TOM Intentions Table'), t)
        df_beliefs = pd.DataFrame(self.tom_beliefs, columns = ['Agent', 'Belief', 'Object', 'Affordance', 'Target'])
        if not df_beliefs.empty:
            self.logger.write_tex(df_beliefs.to_latex(index=False, caption='TOM Beliefs Table'), t)