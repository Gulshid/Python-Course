# 8. Appending Files
#    Append mode adds data at the end without deleting old data.

file_3 = open("Ep_6/program/writefile.txt",  'a')
a = 3
b = 4
file_3.write("\n this is another text in append operation ===>\n")
file_3.write(f"The multiply of two value is : {a * b}")
file_3.close()