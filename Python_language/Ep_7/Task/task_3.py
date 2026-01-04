# Task - 3
try:
    print("*** WELCOME TO EXCEPTION HANDLING TASK NO #3 ***")
    a = int(input("Enter the integer value :"))
    b = input("Enter the string value :")
    
    res = a + b
    print("Result :", res)
    
except ValueError:
    print("*** Error : Please enter the valid integer value ***")
    
    
except TypeError:
    print("*** Error : Type Error ***")