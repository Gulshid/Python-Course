# 6. Local and Global Variables – Understanding variable scope inside functions.
# global variable
z = 20

def func():
    # local variable
    x = 20
    print('The value of x is :',x)


func()
print("the value of z :",z)
