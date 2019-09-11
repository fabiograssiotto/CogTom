# Theory of Mind Module
#
# 
import numpy as np

class ToM:

    # The set of mental states ToM represents.
    MENTAL_STATES = ["BELIEVES"]

    def __init__(self, id, edd, sam):
        self.id = id
        self.edd = edd
        self.sam = sam

    def process(self):
        # Create representations of the mental states 
        # of the form Agent-Mental State-Object

    def print(self):
        print("ToM:")
        print("Agents: ", self.id.agents())
        print("\n")