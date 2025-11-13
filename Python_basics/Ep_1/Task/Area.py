# 12. Write a Program for find the Area of Circle , Triangle, Rectangle

# Area of Circle
pi = 3.14
r = float(input("Enter the value for radius :"))

# formula 
area_circle =  pi * r * r
print("The Area of Circle is : ", area_circle)


print("****************")
# Area of Triangle
base = float(input("Enter the value for Base :"))
height = float(input("Enter the value for Height :"))


# formula 
area_triangle = 0.5 * base * height

print(f"The Area of Triangle is : {area_triangle}")

print("****************")

# Area of Rectangle
length = float(input("Enter the value for length :"))
width = float(input("Enter the value for width :"))

# formula 
area_rectangle = length * width
print(f"The Area of Rectangle is : {area_rectangle}")
