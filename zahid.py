# Zahid - an implementation of the Theory of Mind model
# according to Simon Baron Cohen.
# The intent of this software program is to evaluate false belief tasks.

import pandas as pd

# Basic input for scene
# Reads from format: Actor-sees-Object / Actor-sees-Actor
data = pd.read_csv('environment.txt', sep="\t", comment='#')
