# Utility class for printing out mind modules information.

class MindPrint:

    def __init__(self, id, edd, sam, tom):
        self.id = id
        self.edd = edd
        self.sam = sam
        self.tom = tom

    def print(self, printAll):
        if printAll == True:
            self.id.print()
            self.edd.print()
            self.sam.print()
            self.tom.print(False)
        else:
            self.tom.print(True) # Only Belief Memory
        print()