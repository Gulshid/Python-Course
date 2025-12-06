# 8.Write a function that returns the maximum of three numbers.
def maximium(x, y, z):
    if x > y and x > z:
        print(x, "is max")     
    elif y > x and y > z:
        print(y, "is max")
    elif z > x and z > y:
        print(z, "is max")
        

# function call
maximium(10,8,6)
print("**************")
a = int(input("Enter the value for a :"))
b = int(input("Enter the value for b :"))
c = int(input("Enter the value for c :"))
maximium(a,b,c)
