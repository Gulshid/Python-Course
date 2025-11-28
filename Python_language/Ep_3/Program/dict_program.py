# dict
dic = {"name" : "Gulshid Zada",       "age" : 23, "roll_no" : 391, "pi" : 3.14}

# Method 1
print("Method no 1 :")
print(dic['name'], dic['age'], dic['roll_no'], dic['pi'] )

print("************")
# Method 2
print("Method no 2 :")
for x in dic:
    print(x, ":", dic[x])