# Task - 5
file_1 = None

try:
    file_1 = open("data_file", 'r')
    print(file_1.read())
    
except FileNotFoundError:
    print("*** Error : File not found in directory or folder ***")
    
    
finally:
    if file_1:
        file_1.close()
    print("**** The file is closed Successfully ****")
    
