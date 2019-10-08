print("What phrase do you see?")
response = str(input())
answer = ""
print("\nReversing...")
for position in response:
    answer = position + answer 
    
print("The phrase is "+answer)