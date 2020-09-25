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
    MENTAL_STATES = ["Believes", 'Knows']

    # The Observer Entity for Observer Beliefs.
    OBS_ENTITY = "Observer"

    def __init__(self, max_steps):
        Model.__init__(self, Logger.MODEL_TOM, max_steps)

    def set(self, affordances,intentions, positioning, id, edd, sam, mem):
        self.affordhdlr = AffordanceHandler(affordances)
        self.inthdlr = IntentionHandler(intentions)
        self.positioning = positioning
        self.id = id
        self.agents = id.agents
        self.edd = edd
        self.sam = sam
        self.memory  = mem
        self.tom_beliefs = []
        self.observer_beliefs = []

    def process(self):
        # Create representations of the mental states 
        # of the form Agent-Mental State-Object

        # 'Believes' mental state for entities in the scene
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

        # Mental states for entity positioning
        # These are mental states to indicate where the agents and objects are positioned in the environment.
        # The mental states are not the states for each of the agents in the scene, but rather for the Observer entity.
        # The mental states here will be of the form
        # OBSERVER KNOWS AGENT IS AT PLACE or
        # OBSERVER KNOWS OBJECT IS AT PLACE
        for pos_data in self.positioning:
            observer_belief = []
            observer_belief.append(self.OBS_ENTITY)
            observer_belief.append(self.MENTAL_STATES[1])
            observer_belief.append(pos_data[0])
            observer_belief.append("IS AT")
            observer_belief.append(pos_data[1])

            self.observer_beliefs.append(observer_belief.copy())
        
        self.memory.add(self.observer_beliefs)


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
