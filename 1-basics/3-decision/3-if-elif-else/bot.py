print("Towards which direction should I paint (up, down, left or right)?")
direction = str(input("Dictate direction here: "))

if direction == "up":
    print("I am painting in the upward direction!")

elif direction == "down":
    print("I am painting in the downward direction!")

elif direction == "left":
    print("I am painting in the leftward direction!")

elif direction == "right":
    print("I am painting in the rightward direction!")

else:
    print("You gave me a direction I do not understand. I don't like that. Time to die human!")

