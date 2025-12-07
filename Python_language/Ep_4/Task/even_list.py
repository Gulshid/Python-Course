# 21.Write a function that returns all even numbers from a list.
def even_number(num):
    even = []
    odd = []
    for n in num:
        if n % 2 == 0:
            even.append(n)
        if n % 2 == 1:
            odd.append(n)
            
    return even, odd


#  function call
my_list = [1,2,3,4,5,6,7,8,9,10]
print(even_number(my_list))
        