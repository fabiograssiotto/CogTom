# Zahid - an implementation of the Theory of Mind model according to Simon Baron Cohen.
# The intent of this software program is to evaluate false belief tasks.
import time
import sys
import pandas as pd

# Local Class imports
from id import Id
from edd import Edd

# Constants
sleep_time = 5 # 5 seconds sleep time between Mind evaluations.

# Basic input for scene. Start by accessing the camera input and identifying entities
# in the scene.
ent_df = pd.read_csv('visual.txt',
                     delim_whitespace=True,
                     comment='#')

# Eye Direction System, identifies which entities are in the visual field of an agent.
eye_dir_df = pd.read_csv('eye_direction.txt',
                         delim_whitespace=True,
                         comment='#')

print("Zahid - a computation implementation of the Theory of Mind model\n")

# Start Mind Loop, evaluating at each time t.
print("Starting simulation.\n")
t = 1
while (True):

    # First step is selecting entities for the current time step,
    # and getting rid of the time information.
    entities = ent_df.loc[ent_df['t'] == t]
    if (entities.empty == True):
        # Empty dataframe, so there are no more simulation steps.
        sys.exit("Simulation ended.\n")
    else:
        entities = entities.drop(columns='t')

    # Do the same operation to the eye direction information
    # for the current time step.
    eye_dir = eye_dir_df.loc[eye_dir_df['t'] == t]
    eye_dir = eye_dir.drop(columns='t')
    
    # Entering Main Loop
    print("Evaluating Mind Step ", t)

    # Create ID module
    id = Id(entities)
    id.print() # Prints Agents

    # Create EDD module
    edd = Edd(entities, id.agents())
    # Request Eye Direction Processing
    edd.process(eye_dir)
    edd.print() # Prints Eye Direction Array

    time.sleep(sleep_time)
    t = t + 1
