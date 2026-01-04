# Task - 6
try:
    password = input("Enter the Password :")
    
    if len(password) < 8:
        raise ValueError("Your Password is less than 8 Characters ")
    
    print("Password Accepted :", password)  

except ValueError as e:
    print(f"Error: {e}")
    