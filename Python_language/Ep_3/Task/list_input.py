# # Task 8 a: How to take input from user at runtime in list
list_number = []

n = int(input("Enter the number that you want  :"))

for x in range(n):
    num = int(input("Enter the value :"))
    list_number.append(num)



# method 1 
print(list_number, end= " ")
print("*************")
# method 2
for w in list_number:
    print(w, end= " ")
print()