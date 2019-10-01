print("What type of cover does the book have? (hard or soft)")
cover = str(input("Enter here: "))

if cover == "soft":

    print("Is the book perfect-bound? (yes/no)")
    bound = str(input("Enter here: "))

    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books!")

else:
    print("Books with hard covers can be more expensive!")

