# 4. Function Parameters – Passing values into a function.
def add(x,y):
    print("The additon of two value is :", x + y)
    # return x + y

add(4,5)
# print("The addition of two value is :", add(3,5))


def mul(a,b):
    multiply = a * b
    return multiply


x = int(input("Enter the value for x :"))
y = int(input("Enter the value for y :"))
print("The multiplication of two value is :",mul(x,y))