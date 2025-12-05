# 8. Recursive Functions – Functions that call themselves.
def countdown(n):
    if n == 0:
        print("Done")
        return
    print(n, end = " ")
    countdown(n - 1) # 5 - 1 = 4 | 4 - 1 = 3 | 3 - 1 = 2 | 2 - 1 = 1 | 1 - 1 = 0
    
countdown(5)

# enter = 5
# 