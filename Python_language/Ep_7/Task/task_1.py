# Task - 1
try:
    print("*** WELOCOME TO EXCEPTION HANDLING TASK NO# 1***")
    var_1 = int(input("Enter the first num :"))
    var_2 = int(input("Enter the second num :"))
    
    divide = var_1 / var_2
    print("Diivision of two value is :", divide)
    
except ZeroDivisionError:
    print("*** Error: Cannot divided by Zero! ***")
    