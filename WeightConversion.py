print("1. kg to lbs")
print("2. lbs to kg")

print("")

choice = int(input("Enter your choice : "))

print("")

if choice == 1:
    kg = float(input("Enter weight (kg) : "))
    lbs = kg * 2.20462
    print(f"{kg} kg = {round(lbs,2)} lbs")
elif choice == 2:
    lbs = float(input("Enter weight (lbs) : "))
    kg = lbs / 2.20462
    print(f"{lbs} lbs = {round(kg,2)} kg")
else :
    print("Not a valid choice!")
 