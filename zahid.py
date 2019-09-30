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
from output.mindprint import MindPrint
from output.logger import Logger

# Constants
sleep_time = 2 # 5 seconds sleep time between Mind evaluations.

# Create handler for Environment Inputs
env = Environment()

# Create Belief Memory
memory = BeliefMemory()

# Logger
logger = Logger()
logger.write("Zahid - a computational implementation of the Theory of Mind model", logtoterm = True)
logger.write("Starting simulation. Mind Steps = " + str(env.get_max_time_step()), logtoterm = True)

t = 1
while (True):
    # Set current simulation step.
    if (env.set_time_step(t) == -1):
        logger.write("Simulation ended", logtoterm = True, memorylog = True)
        logger.flush()
        logger.close()
        break

    # Create ID module
    id = Id(env.get_agents(), env.get_drives())

    # Create EDD module
    edd = Edd(env.get_entities(), env.get_agents())
    edd.process(env.get_eye_dir())

    # Create SAM module
    sam = Sam(edd)
    sam.process()

    # Create ToM Module.
    tom = ToM(env.get_affordances(), id, edd, sam, memory)
    tom.process()
    
    # Print out output
    mp = MindPrint(logger, t, id, edd, sam, tom, memory)
    mp.print_header(termlog = True)
    mp.print()

    time.sleep(sleep_time)
    t = t + 1