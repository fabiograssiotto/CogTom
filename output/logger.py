import sys
from pathlib import Path

class Logger(object):
    
    MODULES_MAIN = 'Main'
    MODULES_MODEL = 'Model'
    MODULES_MEMORY = 'Memory'
    MODEL_ID = 'ID'
    MODEL_EDD = 'EDD'
    MODEL_SAM = 'SAM'
    MODEL_TOM = 'TOM'

    def __init__(self, module, steps, model = None):
        self.terminal = sys.stdout
        log_folder = Path("output/log/")
        tex_folder = Path("output/tex/")
        self.modellog = []
        self.modeltex = []
        self.memlog = []
        self.max_step = steps

        if (module == Logger.MODULES_MAIN):
            self.mainlog = open("output\main.log", "w+")
        elif (module == Logger.MODULES_MODEL):
            for i in range(steps):
                log_file = model + "-" + str(i+1) + ".log"
                tex_file = model + "-" + str(i+1) + ".tex"    
                file_name = log_folder / log_file
                file_name_tex = tex_folder / tex_file
                #file_name = "output\\log\\" + model + "-" + str(i+1) + ".log"
                #file_name_tex = "output\\tex\\" + model + "-" + str(i+1) + ".tex"
                self.modellog.append(open(file_name, "w+"))
                self.modeltex.append(open(file_name_tex, "w+"))
        elif (module == Logger.MODULES_MEMORY):
            for i in range(steps):
                self.memlog.append(open("output\memory.log", "w+"))

        self.module = module

    def write(self, message, step, logtoterm = False):
        # Terminal Logs
        if (logtoterm == True):
            self.terminal.write(message + '\n')
        # File Logs
        if (self.module == Logger.MODULES_MAIN):
            # Main logging
            self.mainlog.write(message + '\n')
        elif (self.module == Logger.MODULES_MODEL):
            self.modellog[step-1].write(message + '\n')  
        elif (self.module == Logger.MODULES_MEMORY):
            self.memlog[step-1].write(message + '\n')

    def write_tex(self, message, step):
        self.modeltex[step-1].write(message + '\n')
        
    def flush(self):
        pass    


#    def close(self):
#        if (self.module == Logger.MODULES_MAIN):
#            self.mainlog.close()
#        elif (self.module == Logger.MODULES_MODEL):
#            self.modellog[step-1].close()
#            self.modeltex[step-1].close()
#        elif (self.module == Logger.MODULES_MEMORY):
#            self.memlog[step-1].close()
