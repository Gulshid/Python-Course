# 7. ***args and **kwargs – Using variable-length arguments in functions.
# *args

def add(*num):
    return sum(num)


print("the additon of four value is :", add(3,4,5,6))
print("the additon of ten value is :", add(2,3,4,5,6,1,2,3,6,7))

print("******************")
# **kwargs
def dictionary(**data):
    for a, b in data.items():
        print(a + " : " , b)

dictionary(name = "Muhammad", age = 23)
print("***********")
dictionary(name = "Gulshid Zada", age = 23, depart = "BS CS", Semester = "5th", Grade = 'A+')


