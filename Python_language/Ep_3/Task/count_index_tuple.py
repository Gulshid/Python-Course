# Task 3: Use count() and index()
fruit = ("Apple", "Peach", "Mango", "Banana","Peach", "Mango", "Banana", 1,2,2,2)
print("With bracket display tuple values :")
print(fruit)
print("***********")

print("using loop method :")
for w in fruit:
    print(w, end= " ")
print()

print("***********")
# count function
print("Count function :")
count = fruit.count(2)
print(f"The Fruit Repeat in {count} time ")

print("***********")
# index function
print("Index function  :")
index = fruit.index(2)
print(f"The fruit is present on {index} index")

