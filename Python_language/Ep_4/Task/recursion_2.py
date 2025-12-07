# 15.Write a recursive function to find the sum of numbers 1 to n.
def sum_num(num):
    if num == 1:
        return 1
    
    # recursion 
    return num + sum_num(num - 1) # sum_num(5)=  5 + sum_num(5 - 1) = 5 + sum_num(4) => 5 + 10 = 15
                                #  sum_num(4)= 4 + sum_num(4 - 1) = 4 + sum_num(3) => 4 + 6 = 10
                                #  sum_num(3)= 3 + sum_num(3 - 1) = 3 + sum_num(2) => 3 + 3 = 6
                                #  sum_num(2)= 2 + sum_num(2 - 1) = 2 + sum_num(1) => 2 + 1 = 3
                                #  sum_num(1)= 1


# function call
print(sum_num(4))
print("************")

a = int(input("Enter the value for a :"))
print(sum_num(a))

# enter = 5
# 1 