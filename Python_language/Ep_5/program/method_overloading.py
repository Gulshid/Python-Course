# 10. Method Overloading (conceptual in Python)
class Calculator:
    def add(self, a, b = 0, c = 0):
        return a + b + c
    
# class ==> object
cal = Calculator()
print("The additon of one value input :", cal.add(2))
print("The additon of two value input :", cal.add(2, 4))
print("The additon of three value input :", cal.add(2, 5, 8))