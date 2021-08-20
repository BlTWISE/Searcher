import sys

instances = 0
filename = "filename.txt"
target = "gmail"

with open(filename) as file: 
    for line in file:
        line = line.rstrip()  # remove '\n' at end of line
        if target in line: # modify this condition to your liking
            if True: # you can use this nested condition for further refinement of what you are looking for
                print(str(instances) + ": " + line)
                instances += 1

