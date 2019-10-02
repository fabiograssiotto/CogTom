# Base class for all Model classes
from output.logger import Logger

class Model:
    
    def __init__(self, logger_id):
        # Logging is common to all model classes.
        self.logger = Logger(Logger.MODULES_MODEL, model = logger_id)