# Utility class for printing out mind modules logs.
from output.logger import Logger

class MindPrint:

    def __init__(self, logger, t, id, edd, sam, tom, mem):
        self.logger = logger
        self.t = t
        self.id = id
        self.edd = edd
        self.sam = sam
        self.tom = tom
        self.mem = mem
        
    def print_header(self):
        msg = "Evaluating Mind Step " + str(self.t)
        self.logger.write(msg, memorylog = True)

    def print(self):
        self.id.print(self.logger)
        self.edd.print(self.logger)
        self.sam.print(self.logger)
        self.tom.print(self.logger)
        self.mem.print(self.logger) # Only Belief Memory