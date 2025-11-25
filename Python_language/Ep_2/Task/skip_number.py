# 20. Skip a Specific Number

# Skip a number using:

# continue

for skip in range(1, 21):
    if skip == 2 or skip == 5 or skip == 8 or  skip == 13 or skip == 17 or skip == 20:
        continue # SKip the Specific value 
    print(f"{skip}", end= " ")
    