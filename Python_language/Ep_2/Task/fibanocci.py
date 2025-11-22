# 6. Fibonacci Series

    # 1.Print the Fibonacci series up to n terms

number = int(input("Enter the value for fibanocci Series :"))

a = 0
b = 1

for j in range(number + 1):
    print(a, end= " ")
    # logic 
    c = a + b # c = 1
    a = b  # a = 1
    b = c   # b = 1