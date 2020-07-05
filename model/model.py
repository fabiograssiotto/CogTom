# Base class for all Model classes
from output.logger import Logger

class Model:
    
    def __init__(self, logger_id, steps):
        # Logging is common to all model classes.
        self.logger = Logger(Logger.MODULES_MODEL, steps, model = logger_id)