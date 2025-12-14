# Task 12: Convert file content to uppercase.
file = open("Ep_6/Task/create_file.txt", 'r')
d = file.read()
file.close()

file = open("Ep_6/Task/create_file.txt", 'w')
file.write(d.upper())
file.close()