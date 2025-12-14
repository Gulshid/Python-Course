# Task 13: Remove all empty lines from a file.
file = open("Ep_6/Task/create_file.txt",  'r')
data = file.readlines()
file.close()


f = open("Ep_6/Task/create_file.txt",  'w')
for line in data:
    if line.strip() != "":
        f.write(line)
f.close()