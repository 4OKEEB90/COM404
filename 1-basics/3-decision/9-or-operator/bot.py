print("What type of adventure should I have? (short/long/scary/safe)")
type = str(input("Enter here: "))

if ((type == "short") or (type == "scary")):
    print("Entering the dark forest!")

elif ((type == "long") or (type == "safe")):
    print("Taking the safe route!")

else:
    print("I'm not sure which route to take!")