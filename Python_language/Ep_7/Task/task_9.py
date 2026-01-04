# Task - 9
try:
    print("*** WELCOME TO EXCEPTION HANDLING TASK NO #9 ***")
    a = int(input("Enter the integer value :"))
    b = input("Enter the string value :")
    
    res = a + b
    print("Result :", res)
    
except TypeError:
    print("*** Error : Type Error ***")