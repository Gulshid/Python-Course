# 24.Write a function to count vowels in a string.
def count_vowel(text):
    vowel = 'aeiouAEIOU'
    count = 0
    
    for i in text:
        if i in vowel:
            count += 1
    return count


#  function call
s = 'Hello World'
string = str(input("Enter any words :"))
print("The total vowel in string is :", count_vowel(string))
print("*********")
print("The total vowel in string is :", count_vowel(s))