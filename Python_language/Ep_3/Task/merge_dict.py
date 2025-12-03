# Task 9: Merge two dictionaries
student_info = {
    'name': "Muhammad",
    'age': 23
}
print("Student info dict :")
print(student_info)

print("***********")
student_marks = {
    'science': 89,
    'math': 78
}
print("Student marks dict :")
print(student_marks)


print("***********")
print("Merge two dict values ")
student_info.update(student_marks)
print(student_info)