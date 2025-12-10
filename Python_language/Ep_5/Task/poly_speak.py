# Task 4: Write a program using polymorphism (two classes with same method speak()).
class Teacher:
    def speak(self):
        print("Teacher is Speaking ...")
        


class Student:
    def speak(self):
        print("Student is Speaking ...")
        


def call_speak(p):
    p.speak()
    


# object
t = Teacher()
s = Student()

call_speak(t)
call_speak(s)