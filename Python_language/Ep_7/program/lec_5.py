# lecture 5
try:
    x = float(input("Enter the first value :"))
    y = float(input("Enter the second value :"))
    z = x / y
    print("Z :", z)
    
except ZeroDivisionError:
    print("*** Error : Cannot divided by Zero! ***")
    
except ValueError:
    print("*** Error : Invalid data type value entered ***")
    
else:
    print("*** No Error in Code ***")
    