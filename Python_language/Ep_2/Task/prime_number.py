# 8. Prime Number

    # 1.Check whether a number is prime or not

num = int(input("Enter the value for Prime Number :"))

isPrime = True

if num < 0:
    print(f"{num} ==> There is No Prime Number for Negative Number")
    
elif num == 0 or num == 1:
    print(f"{num} ==> There is NO Prime Number for 0 and 1 ")
    
else:
    for w in range(2, num): # enter : 6 ==> 2,3,4,5
        if num % w == 0:
            isPrime = False
            break
    
    
    
    if(isPrime):
        print(f"The Number {num} is Prime Number ")
    else:
        print(f"The Number {num} is Not a Prime Number ")