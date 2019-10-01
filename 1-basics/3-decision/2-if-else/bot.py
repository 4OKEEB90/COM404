#Ask what kind of activity this is.
print("What type of activity is this?")
#define the variable "activity" as a string variable to be input by the user.
activity = str(input("Please enter the activity to be performed."))
#If statement to give a specific response to "calculate" activity
if activity == "calculate":
    print("Performing calculations...")
#Else statement to giv a generic response to all other activities
else:
    print("Performing activity")
#A print statement to end the process
print("Activity completed!")