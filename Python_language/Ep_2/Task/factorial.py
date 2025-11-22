#  find the factorial of any number 
num = int(input("Enter the value for fact :"))

fact = 1

if num < 0:
    print("There is no Factorial for Negative Number ==>")
elif num == 0 or num == 1:
    print(f"The Factorial of {num} is 1")
else:
    for s in range(2, num + 1):
        fact = fact * s
    print(f"The factorial of {num} is {fact}")