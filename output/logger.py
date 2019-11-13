import sys

class Logger(object):
    
    MODULES_MAIN = 'Main'
    MODULES_MODEL = 'Model'
    MODULES_MEMORY = 'Memory'
    MODEL_ID = 'ID'
    MODEL_EDD = 'EDD'
    MODEL_SAM = 'SAM'
    MODEL_TOM = 'TOM'

    def __init__(self, module, model = None):
        self.terminal = sys.stdout
        if (module == Logger.MODULES_MAIN):
            self.mainlog = open("output\main.log", "w+")
        elif (module == Logger.MODULES_MODEL):
            file_name = "output\model" + model + ".log"
            self.modellog = open(file_name, "w+")
        elif (module == Logger.MODULES_MEMORY):
            self.memlog = open("output\memory.log", "w+")

        self.module = module

    def write(self, message, logtoterm = False):
        # Terminal Logs
        if (logtoterm == True):
            self.terminal.write(message + '\n')
        # File Logs
        if (self.module == Logger.MODULES_MAIN):
            # Main logging
            self.mainlog.write(message + '\n')
        elif (self.module == Logger.MODULES_MODEL):
            self.modellog.write(message + '\n')  
        elif (self.module == Logger.MODULES_MEMORY):
            self.memlog.write(message + '\n')

    def flush(self):
        pass    

    def close(self):
        if (self.module == Logger.MODULES_MAIN):
            self.mainlog.close()
        elif (self.module == Logger.MODULES_MODEL):
            self.modellog.close()
        elif (self.module == Logger.MODULES_MEMORY):
            self.memlog.close()
