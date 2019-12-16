# Query Module
# Allows information from memory to be output to the user of the system.
import pandas as pd
import os
from memory import beliefmem

class Query:

    def __init__(self, mem, env):
        self.mem = mem
        self.env = env

    def select_scene(self):
        # List all scenes the system can analyse.
        folder = "input"
        subfolders = [f.name for f in os.scandir(folder) if f.is_dir() ]

        print("Scenes:")
        i = 1
        for f in subfolders:
            print(str(i) + ": " + subfolders[int(i)-1])
            i = i + 1
        opt = input("Select Scene: ")
        return (subfolders[int(opt)-1])

    def run(self, t):
        # Start Query Module to check understanding of the false belief tasks.
        ret = 0
        if (t == 1):
            self.greet()
        print("This is mind step " + str(t) + ".")
        print("Scene " + str(t) + ": " + self.env.get_scene())
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
        print("This is the list of commands I understand.")
        self.print_help()

    def print_help(self):
        print("To ask me about people: 'p'")
        print("To ask me about objects: 'o'")
        print("To go to the next mind step: 'enter'")
        print("To quit the simulation: 'q'")
        print()
    
    def exec(self):
        opt = input("Enter command: ")
        if (opt == "q"):
            # Quits the simulation
            return -2
        elif (opt == ""):
            # Next mind step
            print()
            return -1
        elif (opt == "p"):
            print("About what person you want to know about?")
            print(self.mem.get_people())
            person = input("")
            print()
            data = self.mem.get_person_beliefs(person)
            if (data.empty):
                print("Sorry, I cannot understand that.")
                return 0
            else:
                str_list = data.to_string(header = False, index = False).split('\n')
                for blf in str_list:
                    # Remove extra whitespaces
                    s = " ".join(blf.split())
                    # Remove 'None' if at the end of the sentence
                    if (s.split()[-1] == 'None'):
                        s = " ".join(s.split()[:-1])
                    print(s)    
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
                return 0
            else:
                str_list = data.to_string(header = False, index = False).split('\n')
                for blf in str_list:
                    # Remove extra whitespaces
                    s = " ".join(blf.split())
                    # Remove 'None' if at the end of the sentence
                    if (s.split()[-1] == 'None'):
                        s = " ".join(s.split()[:-1])
                    print(s)    
                print()
                return 0
        else:
            # Unknown command
            print("Sorry, I cannot understand that.")
            return 0
