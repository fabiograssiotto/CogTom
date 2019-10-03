# Query Module
# Allows information from memory to be output to the user of the system.
import pandas as pd
from memory import beliefmem

class Query:

    def __init__(self, mem):
        self.mem = mem
        
    def greet(self):
        print("Hello, I am Zahid.")
        print("I know about the following people: ", self.mem.get_people())
        print("And about the following objects: ", self.mem.get_objects())
        print()

    def print_options(self):
        print("Please input: ")
        print("1 - to know about people")
        print("2 - to know about objects")
        print("3 - to tell me I can go")
    
    def run(self):
        self.print_options()
        opt = input("")
        print()
        if (opt == "3"):
            print ("Goodbye.")
            return -1
        elif (opt == "1"):
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
        elif (opt == "2"):
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