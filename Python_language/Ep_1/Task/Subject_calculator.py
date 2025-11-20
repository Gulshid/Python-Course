# Write a Program for Making Student Subject  Calculator
name = str(input("Enter Your Name :"))
Roll_no = int(input("Enter your Roll No :"))

#  Four Subject {eng, urdu, islam, science}
eng = float(input("Enter the English Marks : "))
urdu = float(input("Enter the Urdu Marks :"))
islam = float(input("Enter the Islamyiat Marks  :"))
science =float(input("Enter the Science MArks :"))

total_marks = 400
obt_marks = eng + urdu + islam + science

avg = obt_marks / 4

print(f"NAme : {name} .   Roll No : {Roll_no}")
print(f" English Marks : {eng}. Urdu  Marks : {urdu} ")
print(f"Islamyiat Marks : {islam}. Science MArks : {science}")

print(f"Total MArks : {total_marks}.   obtained Marks : {obt_marks}")

print(f"The Average of Student : {avg}")