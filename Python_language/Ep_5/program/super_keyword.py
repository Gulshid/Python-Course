# 14.Super() Keyword
class A:
    def show(self):
        print("Parent Class")
        


class B(A):
    def show(self):
        super().show()
        print("Child Class")
        
        
# class ===> object 
b = B()
b.show()