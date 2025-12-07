# 18.Write a function using *args that returns the sum of all arguments.
def Add(*num):
    return sum(num)

# function call
print("the additon of multiple values  1:",  Add(2,3,4,5,6))
print("************")
print("the additon of multiple values  2:",  Add(2,3,4,5,6,7,8,9,10))