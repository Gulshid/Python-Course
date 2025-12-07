# 14.Write a recursive function to print numbers from n down to 1.

def print_num(z):
    if z == 0:
        return
    print(z, end = " ")
    
    # recursive function
    print_num(z - 1) # 4 - 1 = 3 | 3 - 1 = 2 | 2 - 1 = 1 | 1 - 1 = 0
    
    
#  function call
print_num(8)
print("***********")
var = int(input("Enter the number :"))
print_num(var)

# enter = 4
# 4 3 2 1 