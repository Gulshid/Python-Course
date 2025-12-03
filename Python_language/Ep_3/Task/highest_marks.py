# Task 10: Student marks dictionary (find highest)
student_dict = {
    'Gulshid Zada' : 95,
    'Muhammad': 87,
    'ALi': 80,
    'Sara': 78,
    'Sana': 70,
    'Samad': 75
}

highest_student = max(student_dict,  key = student_dict.get)
print("Highest Marks Student :", highest_student)
print("Highest Marks: ",student_dict[highest_student] )
