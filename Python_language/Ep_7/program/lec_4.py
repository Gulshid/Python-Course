# lecture 4
try:
    # two variable from user at runtime 
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    result = a / b
    print("Result :", result)
    
except ZeroDivisionError:
    print("*** Error: Cannot divided by Zero! ***")
    
except ValueError:
    print("*** Error: Invalid data type value entered ***")
    
