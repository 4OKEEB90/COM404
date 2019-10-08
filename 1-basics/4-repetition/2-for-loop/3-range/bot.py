print("What level of brightness is required?")
response = int(input("an even number representing the brightness level: "))

print("\nAdjusting brightness...")

for brightness in range (2,response + 1,2):
    print("\nBeep's brightness level: "+"*"*brightness)
    print("Bop's brightness level: "+"*"*brightness)
print("\nAdjustments complete!")
