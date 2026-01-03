# lecture 3
try:
    age = int(input("Enter the your Age :"))
    print("User Age :", age)
except ValueError:
    print("*** Error: Invalid data type value entered ***")
    