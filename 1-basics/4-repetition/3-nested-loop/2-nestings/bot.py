print("Enter a sequence of characters consisting of dashes and two markers e.g. \"X----X\".")
seq = str(input())

print("Please enter the character for the marker")
mk = str(input())

for p in range (0,len(seq),1):
    if seq[p] == mk:
        count = 0
    else:
        count += 1
print(str(count))
