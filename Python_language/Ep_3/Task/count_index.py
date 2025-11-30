# Task 6: Use count() and index()
fruits = ["Apple", "Banana", "Peach", "Mango", "Banana", "Apple", "Banana", "Peach", "Mango"]

print("Fruits :>")
# display the list item
for item in fruits:
    print(item, end = " ")
print()
print("******************")

# Count Operation 
print("Count Operation :>")
count_fruits = fruits.count("Banana")
print(f"The Fruit : {count_fruits} times ")


print("*******************")
# Index Operation
print("Index Operation :>")
index_fruit = fruits.index("Mango")
print(f"The Fruit : {index_fruit} index")