# 10. with Statement
#     Automatically closes the file after use.
# Write 
with open("Ep_6/program/writefile.txt", 'w') as file_4:
    file_4.write("This is With Statement \n")
    file_4.write("with statement use for automatically close file \n")
    file_4.write("No need of close ()")
    

# Read
with open("Ep_6/program/writefile.txt", 'r') as file_5:
    content = file_5.read()
    print(content)
