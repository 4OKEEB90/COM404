print("How many live cables must I avoid?")
LiveCables = int(input("Enter here: ")) 
cables = 0

while (cables < LiveCables):
    print("Avoiding...",end="")
    cables += 1 
    print("...Done! "+str(cables)+" live cable avoided!")
  
print("All live cables have been avoided.")