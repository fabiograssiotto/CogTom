# Zahid - an implementation of the Theory of Mind model
# according to Simon Baron Cohen.
# The intent of this software program is to evaluate false belief tasks.
import time
import pandas as pd

# Constants
sleep_time = 5 # 5 seconds sleep time between Mind evaluations.

# Basic input for scene
# Start by accessing the camera input and identifying entities in the scene.
entities = pd.read_csv('visual.txt', sep="\t", comment='#')

# Reads from format: Actor-sees-Object / Actor-sees-Actor
data = pd.read_csv('environment.txt', sep="\t", comment='#')

# Start Mind Loop, evaluating at each time t.
t = 1
while (True):
    print("Evaluating Mind Step ", t)
    time.sleep(sleep_time)
    t = t + 1

