# Task - 10
try:
    print("*** WELCOME TO EXCEPTION HANDLING TASK NO #10 ***")
    num = int(input("Enter the value for num :"))
    result = 20 / num
    
except ZeroDivisionError:
    print("*** Error : Cannot divided by Zero ***")
    
except ValueError:
    print("*** Error : Please enter a valid numeric value ==> integer value ***")
    
else:
    print("Result :", result)

finally:
    print("The Program is Successfully Exccuted ===>")
    