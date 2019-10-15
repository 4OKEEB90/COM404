def display_ladder(steps):
    print("| |")
    for count in range (1,steps+1,1):
        print("***")
        print("| |")


def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    #return steps
    display_ladder(steps)

create_ladder()
#display_ladder(steps)