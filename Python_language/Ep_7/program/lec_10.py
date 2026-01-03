# lecture 10

#    *** Division Program ***
try:
    num_1 = int(input("Enter the first Number :"))
    num_2 = int(input("Enter the second Number :"))
    
    divide = num_1 / num_2
    
except ZeroDivisionError:
    print(" *** Error : Cannot divided by Zero! ***")
    
except ValueError:
    print("*** Error : Please Enter the valid data type value ==> numeric ")
    
else:
    print("Division of two value is :", divide)
    
finally:
    print("*** The Program is Successfully Executed ***")
    