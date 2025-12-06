# 9.Write a function that returns the reverse of a string.
def Reverse(n):
    return n[:: -1]


# function call
print(Reverse("World"))
print("********")

string = str(input("Enter the string value :"))

print(f"The reverse of string {string} is {Reverse(string)}")