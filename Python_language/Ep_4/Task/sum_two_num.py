# 3. Write a function that returns the sum of two numbers.
def add(var_1, var_2):
    # without third variable method
    # return var_1 + var_2
    # return var_1 - var_2 ==? Subtraction

    # with third variable method
    var_3 = var_1 + var_2
    return var_3

# function call
print(f"The additon of two value :{add(3,4)}")
print("******************")
x = int(input("Enter the value for x :"))
y = int(input("Enter the value for y :"))

print(f"The Addition of two value is : {add(x, y)}")