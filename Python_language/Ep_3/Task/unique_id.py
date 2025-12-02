# Task 6: Find common and unique student IDs
SetA = {101, 102, 103}
SetB = {102, 103, 106}

print("Set A :", SetA)
print("Set B :", SetB)

print("*************")
# common
common_id = SetA.intersection(SetB)
print("Common id :",common_id )


print("*************")
unique_id = SetA.symmetric_difference(SetB)
print("Unique Id :",unique_id )