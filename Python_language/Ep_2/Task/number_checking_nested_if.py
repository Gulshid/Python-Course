#2. Same logic using nested if

num = int(input("Enter the value for Num :"))

if num >=0:
    if num > 0:
        print(f"The value {num} is Positive ")
    elif num == 0:
        print(f"The value {num} is Zero ")
    
else:
    print(f"The value {num} is Negative ")