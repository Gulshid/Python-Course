# 14. Loan Eligibility System

# Check loan eligibility using:

# Salary

# Age
age = int(input("Enter Your Age :"))
Income = int(input("Enter Your Salary :"))
credit_score = int(input("Enter Your Credit Score :"))


if age >= 21:
    if Income >= 30000:
        if credit_score >= 650:
            print(" *** You Are Eligible for Loan ***")
            
            if Income >= 50000 and credit_score >= 750:
                loan_amount = 100000
                
            elif Income >= 40000 and credit-score >= 700:
                loan_amount = 75000
                
            elif Income >= 30000 and credit_score >= 650:
                loan_amount = 50000
            else:
                loan_amount = 25000
            
            print(f"The Maximium Loan Amount : {loan_amount}")
        else:
            print(" *** Your Credit Score is Less than 650 ***")
    else:
        print(" *** Your Income is less than 30000 *** ")
        
else:
    print("Your Age is Less than 21")
    print("Your Not Eligible for Loan Amount")
                
                

            