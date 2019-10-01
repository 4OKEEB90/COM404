print("Please enter the first whole number.")
fn = int(input("Enter here: "))
print("Please enter the second whole number.")
sn = int(input("Enter here: "))
print("Please enter the third whole number.")
tn = int(input("Enter here: "))

EvenCount = 0
OddCount = 0

if fn % 2 ==0:
    EvenCount += 1
else:
    OddCount += 1
if sn % 2 ==0:
    EvenCount += 1
else:
    OddCount += 1
if tn % 2 ==0:
    EvenCount += 1
else:
    OddCount += 1

print("There were "+str(EvenCount)+" even numbers and "+str(OddCount)+" odd numbers")



