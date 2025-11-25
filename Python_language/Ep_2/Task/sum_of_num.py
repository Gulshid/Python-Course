# 19. Sum of Numbers

# Calculate sum of first n natural numbers

number = int(input("Enter The n Natural Number :"))

sum = 0
for n in range(1, number + 1):
    sum = sum + n

print(f"The Sum of {number} is : {sum}")

# 1+2+3+4 = 10
# 1 + 2 + 3 + 4 + 5 + 6 = 21