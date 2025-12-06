# 6.Write a function that checks if a number is even or odd.
def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    elif num % 2 == 1:
        print(num, "is Odd")

# function call
n = int(input("Enter the value for n :"))
even_odd(n)
print("***************")
even_odd(10)