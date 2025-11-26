# 16. Movie Ticket Price Calculator
# Based on:
# 1.Age
# 2.Time (matinee/evening)
# 3.Discount (student, senior citizen)

print("*** Movie Ticket System ***\n")
age = int(input("Enter Your Age :"))
time = int(input("Enter the time (1 -- 24 hour) :"))
day = input("Enter the days (monday - sunday) :").strip().lower()

# logic for age 
if age < 13:
    price = 200
elif age >= 65:
    price = 350
else:
    price = 500
    

# logic for time 
if time < 17:
    price -= 50
    

# logic for days
if day == 'thursday':
    price -= 100

print(f"Total Ticket Price : {price}")
    
    


