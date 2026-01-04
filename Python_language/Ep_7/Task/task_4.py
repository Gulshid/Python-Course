# Task - 4
try:
    print("*** WELCOME TO EXCEPTION HANDLING TASK NO #4 ***")
    a = int(input("Enter the value for a :"))
    b = int(input("Enter the value for b :"))
    c = int(input("Enter the value for c :"))
    
    average = (a + b + c) / 3

except ValueError:
    print("*** Error : Please enter the valid integer value ***")

else:
    print("Average :", average)
    print("*** The Program is Successfully Excuted *** ===>")
    