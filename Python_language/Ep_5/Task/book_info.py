# Task 10: Create a class Book with title, author, price and display book info.
class Book:
    
    # Constructor function 
    # method 1
    # def __init__(self, title, author, price):
    #     self.title = title
    #     self.author = author
    #     self.price = price
    
    
    # method 2
    def __init__(self):
        self.title = input("Enter the title of BOOk :")
        self.author = input("Enter the Author of BOOK :")
        self.price = int(input("Enter the Price of BOOK :"))
        
    
    # show function 
    def show(self):
        print(f"BOOK title : {self.title}")
        print(f"BOOK Author : {self.author}")
        print(f"BOOK Price : {self.price}")


# object 
# method 1 ==> Call
# book = Book("Python Basics", "john", 1200)
# method 2 ===> Call
book = Book()
book.show()
