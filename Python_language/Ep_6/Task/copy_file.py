# Task 15: Copy content from one file to another.
file_1 = open("Ep_6/Task/create_file.txt",  'r')
data = file_1.read()
file_1.close()


file_2 = open("Ep_6/Task/destination_file.txt", 'w')
v = file_2.write(data)
file_2.close()