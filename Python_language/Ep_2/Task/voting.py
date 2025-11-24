# 12. Voting Eligibility Program

    # 1.Check if a person is eligible for voting based on age ≥ 18

# Program 1 
Age = int(input("Enter You Age :"))

eligible = 18 - Age

if Age >= 18:
    print("You Are Eligible for Voting ==>")
else:
    print(f"You Are not Eligible for Voting. You Still have {eligible} Year for Vote ")



# Program 2

age = int(input("Enter Your Age :"))

if age >= 18:
    print("You Are ELigible for Voting ")
else:
    print("You Are   Not Eligible for Voting ")