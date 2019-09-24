print("What is your name human?")
Name = str(input())

print("How old are you (in years)?")
Age = int(input())

print("How tall are you (in meters)?")
Height = float(input())

print("How much do you weigh (in kilograms)?")
Weight = float(input())

BMI = Weight / (Height*Height)

print(Name+" you are "+str(Age)+" years old and you bmi is "+str(BMI))

