# 18. Patterns Printing

# Pattern 1: Increasing number pattern
value = int(input("Enter Any Number :"))

for row in range(value + 1):
    for col in range(row):
        # print("*", end= "")
        print(f"{col}", end= " ")
    print()