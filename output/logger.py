import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("output\logfile.log", "w+")

    def write(self, message):
        self.terminal.write(message + '\n')
        self.log.write(message + '\n')  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()