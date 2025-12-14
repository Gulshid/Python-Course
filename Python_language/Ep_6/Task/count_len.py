# Task 5: Count the number of lines in a file.
file = open("Ep_6/Task/create_file.txt",   'r')
v = file.readlines()
print("Totall Lines :", len(v))

file.close()
