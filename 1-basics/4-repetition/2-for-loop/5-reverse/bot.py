print("What phrase do you see?")
response = str(input())
print("\nReversing...\n")
print("\nThe phrase is ",end="")
for position in range (len(response)-1,-1,-1):
    print(response[position],end="")
print("\n")

