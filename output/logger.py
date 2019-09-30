import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("output\module.log", "w+")
        self.memlog = open("output\memory.log", "w+")

    def write(self, message, memorylog = False):
        self.terminal.write(message + '\n')
        if (memorylog == True):
            self.memlog.write(message + '\n')  
        else:
            self.log.write(message + '\n')

    def flush(self):
        pass    

    def close(self):
        self.log.close()
        self.memlog.close()

sys.stdout = Logger()