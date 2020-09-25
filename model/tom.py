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
        self.agt_beliefs = []
        self.obs_beliefs = []

    def process(self):
        # Mental states for the Agents entities
        # 'Believes' mental state for entities in the scene
        # The mental state modeled here produces descriptions in the form
        # AGENT BELIEVES OBJECT AFFORDANCE or
        # AGENT BELIEVES OBJECT AFFORDANCE TARGET_OBJECT (due to an intention)
        for agent in range(self.edd.edd_eyes.shape[0]):
            agt_belief = []
            # For each agent line in edd_eyes
            # Retrieve the list of objects the agent sees.
            agt_belief.append(self.edd.edd_eyes[agent])
            agt_belief.append(self.MENTAL_STATES[0])
            for ent in range(self.edd.edd_agent_store.shape[1]):
                obj = self.edd.edd_agent_store[agent][ent]
                agt_belief.append(obj)
                
                # Check any affordances the entities may have.
                agt_belief = self.affordhdlr.check_affordances(agt_belief)

                # Check if intentions from the environment 
                # are likely to change beliefs.
                agt_belief = self.inthdlr.check_intentions(agt_belief)
                self.agt_beliefs.append(agt_belief.copy())
                del agt_belief[2:] # Only keeps Agent and Belief 

            # Add the list of beliefs at the end to the Belief Memory.
            self.memory.add(self.agt_beliefs)

        # Mental states for the observer entity - positioning
        # These are mental states to indicate where the agents and objects are positioned in the environment.
        # The mental states are not the states for each of the agents in the scene, but rather for the Observer entity.
        # The mental states here will be of the form
        # OBSERVER KNOWS AGENT IS AT PLACE or
        # OBSERVER KNOWS OBJECT IS AT PLACE
        for pos_data in self.positioning:
            obs_belief = []
            obs_belief.append(self.OBS_ENTITY)
            obs_belief.append(self.MENTAL_STATES[1])
            obs_belief.append(pos_data[0])
            obs_belief.append("IS AT")
            obs_belief.append(pos_data[1])

            self.obs_beliefs.append(obs_belief.copy())
        
        self.memory.add(self.obs_beliefs)


    def print(self, t):
        msg = "Evaluating Mind Step " + str(t)
        self.logger.write(msg, t)
        self.logger.write("ToM:", t)
        self.logger.write("Agents: " + str(self.agents()), t)
        self.logger.write("Intentions: " + str(self.inthdlr.getintentions()), t)
        self.logger.write("Agent Beliefs: " + str(self.agt_beliefs), t)
        self.logger.write("Observer Beliefs: " + str(self.obs_beliefs), t)

        # Latex
        df_intentions = pd.DataFrame(self.inthdlr.getintentions(), columns = ['Agent', 'Intention', 'Object','Target'])
        if not df_intentions.empty:
            self.logger.write_tex(df_intentions.to_latex(index=False, caption='TOM Intentions Table'), t)
        df_agt_beliefs = pd.DataFrame(self.agt_beliefs, columns = ['Agent', 'Belief', 'Object', 'Affordance', 'Target'])
        df_obs_beliefs = pd.DataFrame(self.obs_beliefs, columns = ['Agent', 'Belief', 'Object', 'Affordance', 'Target'])
        df_beliefs = pd.concat([df_agt_beliefs, df_obs_beliefs])
        
        if not df_beliefs.empty:
            self.logger.write_tex(df_beliefs.to_latex(index=False, caption='TOM Beliefs Table'), t)
