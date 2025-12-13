# 6. Writing Files
#    Data is written using write() and writelines().

# 2. write 
# write( ) function 
file_1 = open("Ep_6/program/writefile.txt", 'w')

a = 4
b = 6
file_1.write("This is File handling of python ===> \n")
file_1.write("*** Addtion of two value *** \n")
file_1.write(f"the addition of two value : {a + b}\n")


# file_1.close()

# writelines( ) function 
line = ["This is File handling of python ===> \n","*** Addtion of two value *** \n",  f"the addition of two value : {a + b}"]

file_1.writelines(line)
file_1.close()

