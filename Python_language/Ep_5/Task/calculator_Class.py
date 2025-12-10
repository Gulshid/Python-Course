# Task 8: Create a class Calculator with add, sub, mul, div functions.
class Calculator:
    # Constructor 
    # def __init__(self, var_1, var_2):
    #     self.var_1 = var_1
    #     self.var_2 = var_2
    
    def __init__(self):
        self.var_1 = float(input("Enter the value for var_1 :"))
        self.var_2 = float(input("Enter the value for var_2 :"))    
    
    # add function
    def add(self):
        return self.var_1 + self.var_2
    
    # sub function 
    def sub(self):
        return self.var_1 - self.var_2
    
    
    # mul function 
    def mul(self):
        return self.var_1 * self.var_2
    
    # div function
    def div(self):
        return self.var_1 / self.var_2
    
    
# Object 
cal = Calculator()
print("Addition of two value is :", cal.add())
print("Subtraction of two value is :", cal.sub())
print("Multiplicaction of two value is :", cal.mul())
print("Division of two value is :", cal.div())