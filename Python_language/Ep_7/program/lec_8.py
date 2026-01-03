# lecture 8
try:
    x = open("file.txt", 'r')
    print(x.read())
    
except FileNotFoundError:
    print("*** Error : File not exist in directory ***")
    