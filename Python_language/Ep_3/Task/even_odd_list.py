# Task 8 b: Create list from user input (separate even and odd numbers)
lists = []

even_list = []
odd_list = []

x = int(input("Enter the Number that you want :"))

for var in range(x):
    num = int(input("Enter the value :"))
    lists.append(num)

# display the full list 
print("List :")
print("************")
print(lists)

for i in lists:
    print(i, end= " ")
print()
print("************")



# Even  and Odd Operation
for q in lists:
    if q % 2 == 0:
        even_list.append(q)
    else:
        odd_list.append(q)


print("******Even and Odd list**********")
print(even_list)
print(odd_list)

print("*******Even List*********")
for a in even_list:
    print(a, end= " ")
print()


print("*******Odd List*********")
for a in odd_list:
    print(a, end= " ")
print()


        



