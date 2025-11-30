# Task 7: Copy and join lists
my_list_1 = [1,2,3,4,5]
my_list_2 = my_list_1.copy()

print("Copy Operation :>")
# Copy Operation
print("List 1:")
for x in my_list_1:
    print(x, end = " " )
print()



print("**********")
print("List 2:")
for x in my_list_2:
    print(x, end = " " )
print()

print("**********************************")
print("Join Operation :>")
# Join Operation


x = [1,2,3]
y = [4,5,6]

combine_list = x + y
print(f"x : {x} , y : {y} , join :{combine_list}" )
print("***************")


print("loop :")
print("List x :")
for i in x:
    print(i, end = " ")
print()

print("List y :")
for i in y:
    print(i, end = " ")
print()


print("List of Combine :")
print("Joined List : ",combine_list )