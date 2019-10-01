print("Please enter the first number.")
fn = float(input("Enter here:"))
print("Please enter the second number.")
sn = float(input("Enter here:"))

if fn < sn:
    print("The first number is the smallest!")
elif sn < fn:
    print("The second number is the smallest!")
else:
    print("Both are equal!")

