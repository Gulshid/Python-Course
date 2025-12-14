# Task 7: Count the number of characters in a file.
data = open("Ep_6/Task/create_file.txt", 'r')

count = data.read()
print("Total Characters :", len(count))

data.close()