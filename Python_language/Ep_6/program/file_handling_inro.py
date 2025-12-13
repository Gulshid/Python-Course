#                       ||*** Lecture 1:. File Handling ***||

#    File handling is used to store and manage data permanently in files.

# File handling in Python means creating, opening, reading, writing, and editing files
# stored on a computer.
# A file is a place on secondary storage (HDD/SSD) where data is saved permanently,
# such as:









#                        ||*** 2. Types of Files ***||

#    Common files include text files, CSV files, and log files.
# 1 .txt (text file)
# 2 .csv (comma-separated values)
# 3 .xlsx (Excel)
# 4 .pdf
# 5 .json, etc.
# When your program needs to store, retrieve, or update data, it uses file handling.










#                        ||***  3. Need of File Handling ***||

#  Why Do We Use File Handling?
# We use file handling because:
# 1.  To store data permanently (not lost when program ends)
# 2.  To read saved data later
# 3.  To share data between programs
# 4.  To keep records/logs
# 5.  For data analysis & reporting
# Example uses:
# 1 Student records
# 2 Exam results
# 3 Application logs
# 4 Reports
# 5 User accounts




#                      ||*** 4. File Modes ***||
#    r (read), w (write), a (append), x (create), + (read/write).
#  File Modes in Python
# When opening a file, Python uses different modes:

# Mode Meaning
# 'r' : Read 
# 'w' : Write
# 'a' : append
# 'x' : create a new file
# 'b' : binary
# '+' : Read + write


#                ||*** 5. Opening a File ***||
#    Files are opened using the open() function.
# Example : file = open("data.txt", "r")
var_1 = open("Ep_6/Task/file_1.json", 'x')