# Task 14: Find the longest word in a file.
fi = open("Ep_6/Task/create_file.txt",  'r')
words = fi.read().split()
fi.close()


longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
        


print("Longest word :", longest)
    