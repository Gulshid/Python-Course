# 13 Write a Program for Conversion of Celsius and Fahrenheit with each Other
print("*** Fahrenheit Conversion ***")
cel = float(input("Enter the value for Celsius :"))

#  formula of Fahrenheit 
Fahrenehit = cel * 9 / 5 + 32
print(f"The Fahrenheit of : {cel} is : {Fahrenehit}")

print("*** Celsius Conversion *** ")
fah = float(input("Enter the value for Fahrenheit :"))

# formula of Celsius
Celsius = (fah - 32) * 5 / 9
print(f"The Celsius of :{fah} is : {Celsius}")