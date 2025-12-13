# 7. Reading Files
#    Data is read using read(), readline(), and readlines().

file_Value = open("Ep_6/program/writefile.txt",  'r')

# read(),
content = file_Value.read()

print("Using read() : \n",content)
file_Value.seek(0)
print("**************")



# readline(),
line_1 = file_Value.readline()
print("Using readline :\n", line_1)

line_2 = file_Value.readline()
print("\n ", line_2)


file_Value.seek(0)
print("**************")
# readlines().
lines = file_Value.readlines()
print("Using readlines() \n:", lines)

