def Box(word):
    print("\n*"+"*"*(len(word))+"*")
    print("*"+str(word)+"*")
    print("*"+"*"*len(word)+"*")





def run():
    print("Enter a word:")
    word = str(input())
    Box(word)

run()
