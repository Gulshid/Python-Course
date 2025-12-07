# 20.Write a function that takes both *args and **kwargs together.

def showData(*num, **value):
    print("Args :", num)
    print("Kwargs :", value)
    
    
# function call
showData(1,2,3,4,5,name = "Gulshid Zada", age = 23, marks = 450)