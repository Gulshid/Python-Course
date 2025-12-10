# Task 5: Create a class BankAccount with deposit() and withdraw() functions.
class bankAccount:
    def __init__(self):
        self.balance = 0
        
    def deposite(self, amount):
        self.balance += amount
        print("Successfully Deposited ==> ")
        print(f"Deposite Amount : {amount}")
        print(f"Account Balance : {self.balance}")
        
        
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successfully Withdraw the Amount. {amount}")
            print(f"Account Balance : {self.balance}")
        else:
            print("Insufficient Balance for withdrawal ")
            print(f"Account Balance : {self.balance}")
            
        
        
        
# object 
acc = bankAccount()
acc.deposite(500)


acc.withdraw(300)
acc.withdraw(300)