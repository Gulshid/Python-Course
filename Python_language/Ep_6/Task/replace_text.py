# Task 11: Replace a word in a text file.
file = open("Ep_6/Task/create_file.txt",  'r')
data = file.read()

file.close()

data = data.replace("Coding", "Programming")
data = data.replace("World", "Welcome")

file_4 = open("Ep_6/Task/create_file.txt", 'w')
d = file_4.write(data)
file_4.close()