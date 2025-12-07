# 16.Write a recursive function to find the factorial of a number.
def fact(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return -1
    else:
        # recursion function
        return n * fact(n - 1)   #fact(4) =  4 * fact(4 - 1)  => 4 * fact(3) => 4 * 6 = 24
                                # fact(3) =  3 * fact(3 - 1) => 3 * fact(2) =>  3 * 2 = 6
                                # fact(2) =  2 * fact(2 - 1) => 2 * fact(1) => 2 * 1 = 2
                                # fact(1) =  1
    
    
# function call
print(f"The factorial of number is : {fact(4)}") # n! = 4! = 4 * 3 * 2 * 1 = 24
print("************")
num = int(input("Enter the value for num :"))
print(f"The factorial of {num} is {fact(num)}")

# enter = 4 
# Answer = 24