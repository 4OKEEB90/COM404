print("Where should I look? (bathroom/bedroom/lab)")
where = str(input("Enter here: "))

if where == "bedroom":

    print("Where in the bedroom should I look?")
    bedroom = str(input("Enter here: "))

    if bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

elif where == "bathroom":

    print("Where in the bathroom should I look? (in the bath tub)")
    bathroom = str(input("Enter here: "))

    if bathroom == "in the bath tub":
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")

elif where == "lab":
    print("Where in the lab should I look?")
    lab = str(input("Enter here: "))

    if lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but I will keep looking.")

