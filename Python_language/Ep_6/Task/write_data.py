# Task 2: Write data into a text file.
# method 1
file_1 = open("Ep_6/Task/create_file.txt",  'w')
file_1.write("Hello WOrld \n")
file_1.write("*** Welcome to FIle Handling Task ***\n")
x = 3
y = 8
file_1.write(f"The multiply of two value is : {x * y}\n")
file_1.close()


# method 2
file_2 = open("Ep_6/Task/create_file.txt",  'w')
a = 3
b = 4
line = ["Hello WOrld \n", "*** Welcome to FIle Handling Task ***\n",  f"The add of two value is : {x + y}\n"]
file_2.writelines(line)
file_2.close()



