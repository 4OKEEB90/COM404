print("How many bars should be charged?")
bars = int(input("Enter here: "))
print("")
charge = 0

while (charge < bars):
    charge += 1
    print("Charging: "+"█"*charge)
print("")
print("The battery is fully charged.")