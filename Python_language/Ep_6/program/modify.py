# 11. File Modification
#     Files are modified by reading and rewriting.
# Read operation
file_1 = open("Ep_6/program/writefile.txt", 'r')
content = file_1.read()

file_1.close()

content = content.replace("This is With Statement", "C++ Programming")

file_2 = open("Ep_6/program/writefile.txt", 'w')
file_2.write(content)

file_2.close()
print("Successfully Modified ===>")

