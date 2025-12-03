# Task 11: Product & price dictionary (calculate bill)
products = {
    'apple' : 50,
    'banana' : 40,
    'peach' : 60,
    'mango' : 80,
    'orange' : 75,
}

item = input("Enter the Fruits Product name :")

quantity = int(input("Enter the quantity :"))

bill = products[item] * quantity

print(f"The final bill : {bill}")
