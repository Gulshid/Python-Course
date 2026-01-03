# lecture 9
try:
    age = int(input("Enter your age :"))
    if age < 0:
        raise ValueError("*** Age Cannot be Negative ***")
    print("Age :", age)
    
except ValueError as x:
    print(f"Error : {x}")
    