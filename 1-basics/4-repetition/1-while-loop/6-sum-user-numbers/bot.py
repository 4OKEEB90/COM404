print("How many numbers should I sum up?")
n = int(input())
q = 0
t = 0

while (q < n):
    q+=1
    print("Please enter number "+str(q)+" of "+str(n)+":")
    a = float(input())
    t += a

print("The answer is "+str(t))
