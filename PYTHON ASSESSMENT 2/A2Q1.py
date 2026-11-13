units = int(input("Enter electricity units: "))
ration = input("Ration card (yes/no): ")
age = int(input("Enter highest family member age: "))

# Using separate if statements
if units <= 100:
    print("Full Subsidy")

if 101 <= units <= 200 and ration == "yes":
    print("Partial Subsidy")

if units > 200 and age <= 80:
    print("No Subsidy")

# Using if-elif-else
if units <= 100:
    print("Full Subsidy")
elif 101 <= units <= 200 and ration == "yes":
    print("Partial Subsidy")
elif units > 200 and age > 80:
    print("Senior Citizen Subsidy")
else:
    print("No Subsidy")
