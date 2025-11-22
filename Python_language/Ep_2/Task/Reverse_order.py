# 4. Reverse Display

    # 1.Display a list or number series in reverse order
value = int(input("Enter the value :"))
reverse = 0

while value > 0:
    digit = value % 10 # =  123.4 , 12.3, 1.2, 1
    reverse = reverse * 10 + digit
    value = value // 10

print(f"{reverse}")