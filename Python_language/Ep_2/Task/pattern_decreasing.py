# 18. Patterns Printing
# Pattern 2: Decreasing number pattern

n = int(input("Enter Any Number :"))

for x in range(n, 0, -1):
    for y in range(x+1):
        # print("*", end= " ")
        print(f"{y}", end= " ")
    print()