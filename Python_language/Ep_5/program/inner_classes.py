# 13.Inner Classes
class Outer:
    def show_1(self):
        print("Outer Class function Created")
        
    class Inner:
        def show_2(self):
            print("Inner Class function Created")
            


# class ===> object
o = Outer()
o.show_1()


i = Outer.Inner()
i.show_2()