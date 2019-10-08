print("What strange markings do you see?")
user_word = str(input(""))
print("\nIdentifying...")

for position in range (0,len(user_word),1):
    print("index "+str(position)+":"+user_word[position]+" ")
print("\nDone!")