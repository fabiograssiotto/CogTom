# Zahid - an implementation of the Theory of Mind model according to Simon Baron Cohen.
# The intent of this software program is to evaluate false belief tasks.
import time
import sys
import pandas as pd

# Local Class imports
from model.id import Id
from model.edd import Edd
from model.sam import Sam
from model.tom import ToM
from memory.beliefmem import BeliefMemory
from input.environment import Environment
from output.logger import Logger
from query.query import Query

# Create handler for Environment Inputs
env = Environment()

# Create Belief Memory
memory = BeliefMemory()

# Create Query module
query = Query(memory, env)

# Create Model modules instances
id = Id()
edd = Edd()
sam = Sam()
tom = ToM()

# Logger
logger = Logger(module = Logger.MODULES_MAIN)
logger.write("Zahid - a computational implementation of the Theory of Mind model", logtoterm = True)
logger.write("", logtoterm = True)
logger.write("Starting simulation. Mind Steps = " + str(env.get_max_time_step()), logtoterm = True)

t = 1
while (True):
    # Set current simulation step.
    if (env.set_time_step(t) == -1):
        logger.write("Simulation ended", logtoterm = True)
        break

    # Start ID module
    id.set(env.get_agents())

    # Start EDD module
    edd.set(env.get_entities(), env.get_agents())
    edd.process(env.get_eye_dir())

    # Start SAM module
    sam.set(edd)
    sam.process()

    # Start ToM Module.
    tom.set(env.get_affordances(), env.get_intentions(), id, edd, sam, memory)
    tom.process()
    
    # Print out outputs from all modules and memory.
    id.print(t)
    edd.print(t)
    sam.print(t)
    tom.print(t)
    memory.print(t)

    # Starting query module
    logger.write("Starting query module, mindstep = " + str(t))
    if (query.run(t) == -2):
        # Quits
        logger.write("Simulation ended", logtoterm = True)
        break
    # Update time step
    t = t + 1

# Housekeeping
logger.flush()
logger.close()
