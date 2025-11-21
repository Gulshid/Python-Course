#1. Check if a number is greater, less, or equal to zero using if–elif–else
number = int(input("Enter the value for Number :"))

if number > 0:
    print(f"The Number {number} is Positive")
elif number < 0:
    print(f"The Number {number} is Negative")
else:
    print(f"The Number {number} is Zero")