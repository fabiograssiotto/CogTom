# Zahid - an implementation of the Theory of Mind model according to Simon Baron Cohen.
# The intent of this software program is to evaluate false belief tasks.
import time
import pandas as pd

# Local Classes imports
from id import Id

# Constants
sleep_time = 5 # 5 seconds sleep time between Mind evaluations.

# Basic input for scene. Start by accessing the camera input and identifying entities
# in the scene.
ent_df = pd.read_csv('visual.txt',
                     delim_whitespace=True,
                     comment='#')

# Start Mind Loop, evaluating at each time t.
t = 1
while (True):
    print("Evaluating Mind Step ", t)

    # First step is selecting entities for the current time step.
    entities = ent_df.loc[ent_df['t'] == t]
    
    # Create ID
    id = Id(entities)
    id.print()

    time.sleep(sleep_time)
    t = t + 1
