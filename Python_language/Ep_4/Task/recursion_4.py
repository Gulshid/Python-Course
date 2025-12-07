# 17.Write a recursive function to find the fibonocci of n series
def fibonocci(x):
    if x <= 1:
        return 1
    else:
        # recursion function
        return fibonocci(x - 1) + fibonocci(x - 2) # fib(5) = fib(5 - 1) + fib(5 - 2) => fib(4) + fib(3)=> 5 + 3 = 8
                                        #   fib(4) = fib(4 - 1) + fib(4 - 2) => fib(3) + fib(2) => 3 + 2 = 5
                                        #   fib(3) = fib(3 - 1) + fib(3 - 2) => fib(2) + fib(1) => 2 + 1 = 3
                                        #   fib(2) = fib(2 - 1) + fib(2 - 2) => fib(1) + fib(0) => 1 + 1 = 2
                                        #   fib(1) = 1
                                        #   fib(0) = 1
    
# function call
print("Fibonocci :",fibonocci(5))
print("*********")
v = int(input("Enter the value :"))
print(f"Fibonocci :",fibonocci(v))

# enter = 5 
# Answer = 8