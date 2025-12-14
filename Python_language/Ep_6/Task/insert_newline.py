# Task 10: Insert a new line at a specific position in a file.
data = open("Ep_6/Task/create_file.txt",  'r')

d = data.readlines()

data.close()

d.insert(1, "\nHello World \n")
d.insert(0, "\n a + b = 5 \n" )
d.insert(2, "*** Coding ***\n")


data = open("Ep_6/Task/create_file.txt",  'w')
val = data.writelines(d)
data.close()