# 25.Write a function to check if a number is prime.
def Prime(num):
    if num < 0:
        print(f"There is no Prime Number for Negative value {num}")
    elif num == 0 or num == 1:
        print(f"{num} is not a Prime Number")
        
    else:
        isprime = True
        
        for x in range(2, num):
            if num % x == 0:
                isprime = False
                break
            
                
        
        if (isprime):
            print(f"{num} is Prime Number ")
        else:
            print(f"{num} is Not Prime Number ")


# function call
Prime(3)
print("***********")
number = int(input("Enter any Number :"))
Prime(number)