# 10. Student Marks System
# Calculate:
# Total
# Average
# Percentage
# Grade
print("******* Student Marks System ******** \n")
print("******* Enter the Subjects Marks ********* \n")

eng = int(input("Enter the English Marks :"))

urdu = int(input("Enter the Urdu Marks :"))

islam = int(input("Enter the Islamyiat Marks :"))

phy = int(input("Enter the Physics Marks :"))

chem = int(input("Enter the Chemistry Marks :"))

computer = int(input("Enter the Computer Science Marks :"))


total_marks = 600
obt_marks = eng + urdu + islam + phy + chem + computer

Persentage = (obt_marks / total_marks) * 100
Average = obt_marks / 6

if Persentage >= 90:
    grade = 'A+ => Passed'
    
elif Persentage >= 80:
    grade = 'A => Passed'
elif Persentage >= 70:
    grade = 'B => Passed'
elif Persentage >= 60:
    grade = 'C => Passed'
elif Persentage >=55:
    grade = 'D => Passed'
elif Persentage >= 50:
    grade = 'E => Passed'
else:
    grade = 'F => Failed'
    
    
print("******* Record Of Student Marks System *****\n")
print(f"English : {eng},    Urdu : {urdu},   Islamyiat : {islam}\n")
print(f"Physics : {phy},    Chemistry : {chem},   Computer Science : {computer}\n")

print(f"Out of : {total_marks}. Student Obtained Marks : {obt_marks} \n")
print(f"Persentage : {Persentage},   Average : {Average}")

print("The Student Grade is : ", grade)
