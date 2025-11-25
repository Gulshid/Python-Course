# 13. Student Grading System (Multiple Criteria)
# Grade by:
# Marks
# Attendance

marks = float(input("Enter Your Marks (0 to 100) :"))
attendence = float(input("Enter Your Attendence :"))


if marks >= 40:
    if attendence >= 75:
        print("*** Student is Passed ==>")
        
        if marks >= 90:
            grade = 'A+'
        elif marks >= 80:
            grade = 'A'
        elif marks >=70:
            grade ='B'
        elif marks >=60:
            grade ='C'
        elif marks >= 50:
            grade = 'D'
        elif marks >= 40:
            grade = 'E'
        else:
            grade = 'F'
        
        print(f"The Student Grade : {grade}")
    else:
        print("Sudent Attendence is less than 75 =>")
        
else:
    print("The Student Marks is less than 40 =>")
