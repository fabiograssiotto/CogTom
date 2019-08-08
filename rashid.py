# Rashid - an implementation of the Theory of Mind model
# according to Simon Baron Cohen.
# The intent of this software program is to evaluate false belief tasks.

# Basic input for scene
num_actors = input("Enter the number of actors\n")
actors = list()
objects = list()
for i in range(int(num_actors)):
    actor = input("Enter Actor #" + str(i+1) + ": ")
    actors.append(actor)
num_objects = input("Enter the number of objects\n")
for i in range(int(num_objects)):
    object = input("Enter Object #" + str(i+1) + ": ")
    objects.append(object)
