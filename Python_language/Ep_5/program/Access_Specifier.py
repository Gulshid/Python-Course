# 2. Access Specifiers
    # {Public , Protected , private } ===> Access Specifier 

class Example:
    
    # public Access Specifier
    var_1 = "I am Public Access Specifier"
    
    # protected Access Specifier
    _var_2 = " I am Protected Access Specifier"
    
    # private Access Specifier
    __var_3 = "I am private Access Specifier"
    
    
    def show(self):
        print("Public :", Example.var_1)
        print("Protected :", Example._var_2)
        print("Private :", Example.__var_3)
        
        


# object 
obj = Example()
obj.show()

print(obj.var_1)
print(obj._var_2) # Work but not recommended
# print(obj.__var_3)