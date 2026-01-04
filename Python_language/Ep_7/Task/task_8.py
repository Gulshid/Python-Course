# Task - 8
try:
    filename = input("Enter the file name :")
    file_read = open(filename, 'r')
    print(file_read.read())
    
except FileNotFoundError:
    print("**** Error : The File is Not found in directory or folder ****")