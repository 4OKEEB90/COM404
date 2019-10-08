print("Please enter a number:")
n = int(input())
total = 1
while (n > 0):
    total *= n
    n -= 1

print("The factorial is "+str(total))
