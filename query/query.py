# Query Module
# Allows information from memory to be output to the user of the system.
import pandas as pd
from memory import beliefmem

class Query:

    def __init__(self, mem):
        self.mem = mem
    
    def run(self, t):
        # Start Query Module to check understanding of the false belief tasks.
        ret = 0
        if (t == 1):
            self.greet()
        print("This is mind step " + str(t))
        while (True):
            # Run until the user is satisfied, or quits the program.
            res = self.exec()
            if (res != 0):
                ret = res
                break
        return ret

    def greet(self):
        print("Hello, I am Zahid.")
        print()
        print("List of commands I understand:")
        self.print_help()

    def print_entities(self):
        print("I know about the following people: ", self.mem.get_people())
        print("And about the following objects: ", self.mem.get_objects())
        print()

    def print_help(self):
        print("p - to ask me about people")
        print("o - to ask me about objects")
        print("g - to keep going")
        print("q - quit")
        print()
    
    def exec(self):
        opt = input("Enter command: ")
        if (opt == "q"):
            return -2
        elif (opt == "g"):
            return -1
        elif (opt == "p"):
            print("About what person you want to know about?")
            print(self.mem.get_people())
            person = input("")
            print()
            data = self.mem.get_person_beliefs(person)
            if (data.empty):
                print("Sorry, I cannot understand that.")
                return -1
            else:
                print(data.to_string(header = False, index = False))
                print()
                return 0
        elif (opt == "o"):
            print("About what object you want to know about?")
            print(self.mem.get_objects())
            object = input("")
            print()
            data = self.mem.get_object_beliefs(object)
            if (data.empty):
                print("Sorry, I cannot understand that.")
                return -1
            else:
                print(data.to_string(header = False, index = False))
                print()
                return 0
        else:
            # something wrong.
            print("Sorry, I cannot understand that.")
            return -1
