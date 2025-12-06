# 4.Write a function that takes two numbers and returns their product.
def product(x , y):
    return x * y
    # return x / y 


# function call
print("The product of x and y :", product(13,5))
print("******************")
a = int(input("Enter the value for a :"))
b = int(input("Enter the value for b :"))
print(f"The product of {a} and {b} is : {product(a, b)}")
