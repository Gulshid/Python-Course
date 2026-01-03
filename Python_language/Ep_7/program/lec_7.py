# lecture 7
number = [1,2,3]

try:
    print(number[4])
    
except IndexError:
    print("*** Error: Invalid Index ***")
    