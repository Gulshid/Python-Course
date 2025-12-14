# Task 8: Append data to an existing file.
data = open("Ep_6/Task/create_file.txt",   'a')

data.write("\nHello \n")
a = 10
b = 6
data.write(f"The sub of two value is : {a - b}")

data.close()