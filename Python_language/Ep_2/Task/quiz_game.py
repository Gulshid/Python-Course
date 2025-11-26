# 15. Interactive Quiz Game

# Ask MCQs and display score

print("*** Welcome to Quiz Game *** \n")
print("*** Enter the Following Option iin MCQs ***\n")

score = 0

print("1. What is the Capital of France ?")
print("A. Berline")
print("B. Paris")
print("C. Rome")


ans = input("Enter Your Answer :").lower()

if ans == 'b':
    print("*** Correct ANswer ***")
    score += 1
else:
    print("Wrong Answer The Correct One is B")
    
print("2. Which language is used for styling in web page  ?")
print("A. HTML")
print("B. Python")
print("C. CSS")

ans = input("Enter Your Answer :")

if ans == 'c':
    print("*** Correct Answer ***")
    score +=1
    
else:
    print("Wrong Answer The Correct One is C")


print("3. What is the Output of 2 ** 3 ?")
print("A. 6")
print("B. 8")
print("C. 12")

ans = input("Enter Your Answer :").lower()

if ans == 'b':
    print("*** Correct Answer ***")
    score += 1
else:
    print("Wrong Answer The Correct One is B")
    
    
print("4. WHich Planet is Known as Red Planet ?")
print("A. Earth")
print("B. Mars")
print("C. Jupitor")

ans = input("Enter Your Answer :").lower()

if ans == 'b':
    print("*** Correct Answer ***")
    score += 1
else:
    print("Wrong Answer The Correct One is B")
    
    
    
print("5. WHich of the following is programming Languages  ?")
print("A. HTML")
print("B. CSS")
print("C. JavaScript")

ans = input("Enter Your Answer :").lower()

if ans == 'c':
    print("*** Correct Answer ***")
    score += 1
else:
    print("Wrong Answer The Correct One is C")
    
    
print("You are Score is : ", score)