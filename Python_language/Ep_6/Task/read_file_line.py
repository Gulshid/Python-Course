# Task 4: Read a file line by line.
file_val = open("Ep_6/Task/create_file.txt",  'r')

read_line = file_val.readline()
print("Every line :\n", read_line)

r = file_val.readline()
print(r)

a = file_val.readline()
print(a)

file_val.close()