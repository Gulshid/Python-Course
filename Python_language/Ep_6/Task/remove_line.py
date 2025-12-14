# Task 9: Remove a specific line from a file.
data = open("Ep_6/Task/create_file.txt",   'r')
lines = data.readlines()
data.close()

# delete a specific line
del lines[4]

del lines[0]

data = open("Ep_6/Task/create_file.txt", 'w')
c = data.writelines(lines)
print(c)
data.close()

