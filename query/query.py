# Query Module
# Handles user interaction.
import pandas as pd
from memory import beliefmem

class Query:

    def __init__(self, mem, env):
        self.mem = mem
        self.env = env

    def select_scene(self, scenes):
        print("Scenes:\n")
        i = 1
        for f in scenes:
            print(str(i) + ": " + f)
            i = i + 1
        print()
        opt = input("Select Scene (q to quit): ")
        print()
        if (opt == "q"):
            print("Goodbye.")
            exit()
        return (scenes[int(opt)-1])

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
        print("Hello, I am CogTom.")
        print()
        print("This is the list of commands I understand.")
        self.print_help()

    def print_help(self):
        print("To ask me about people: 'p'")
        print("To ask me about things: 'o'")
        print("To ask me about the Observer: 'o'")
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
        elif (opt == "t"):
            print("About which thing you want to know about?")
            print(self.mem.get_things())
            object = input("")
            print()
            data = self.mem.get_thing_beliefs(object)
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
            data = self.mem.get_observer_beliefs()
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
