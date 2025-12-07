# 19.Write a function using **kwargs that prints all key–value pairs.
def dictionary_values(**n):
    for a, b in n.items():
        print(a + " : ", b)

# function call
dictionary_values(name = "Gulshid Zada", age = 23, grade = 'A+', Semester = 5)