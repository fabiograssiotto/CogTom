# CogTom - an implementation of the Theory of Mind model according to Simon Baron Cohen.
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
from environment.environment import Environment
from output.logger import Logger
from query.query import Query

# Create handler for Environment Inputs
env = Environment()

# Create Belief Memory
memory = BeliefMemory()

# Create Query module
query = Query(memory, env)

# Select scenario to be analysed.
sc = query.select_scene(env.get_scenes())
env.set_scene(sc)

max_steps = env.get_max_time_step()

# First time step
t = 1

# Main Module Logger
logger = Logger(Logger.MODULES_MAIN, max_steps, None)
logger.write("", t, logtoterm = True)
logger.write("CogTom - a computational implementation of the Theory of Mind model", t, logtoterm = True)
logger.write("", t, logtoterm = True)

logger.write("Starting simulation. Mind Steps = " + str(max_steps), t, logtoterm = True)

# Create Model modules instances
id = Id(max_steps)
edd = Edd(max_steps)
sam = Sam(max_steps)
tom = ToM(max_steps)
memory.set(max_steps)


while (True):
    # Set current simulation step.
    if (env.set_time_step(t) == -1):
        logger.write("Simulation ended", 1, logtoterm = True)
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
    tom.set(env.get_affordances(),
            env.get_intentions(), 
            env.get_positioning(),
            id, edd, sam, memory)
            
    tom.process()
    
    # Print out outputs from all modules and memory.
    id.print(t)
    edd.print(t)
    sam.print(t)
    tom.print(t)
    memory.print(t)

    # Starting query module
    logger.write("Starting query module, mindstep = " + str(t), t)
    if (query.run(t) == -2):
        # Quits
        logger.write("Simulation ended", t, logtoterm = True)
        break

    # Update time step
    t = t + 1

logger.flush()
