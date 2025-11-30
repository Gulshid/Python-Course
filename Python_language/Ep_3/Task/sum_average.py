# Task 11: Calculate sum and average
number = []
n = int(input("Enter the number that you want :"))

for x in range(n):
    user_input = float(input(f"Enter the value for {x + 1} :"))
    number.append(user_input)
    
    
Sum = sum(number)
Average = Sum / n

print("List : ", number)
print("SUm : ", Sum)
print("Average :", Average)
