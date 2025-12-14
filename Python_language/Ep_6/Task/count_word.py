# Task 6: Count the number of words in a file.
f = open("Ep_6/Task/create_file.txt",  'r')
value = f.read()
words = value.split()

print(" Words :", words)
print("Total Words:", len(words))