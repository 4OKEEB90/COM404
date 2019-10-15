def sum_weights(Weight_Beep,Weight_Bop):
    Sum = Weight_Beep + Weight_Bop
    return Sum

def calc_avg_weight(Weight_Beep,Weight_Bop):
    Avg = (Weight_Beep * Weight_Bop) / 2
    return Avg

def run():
    print("What is the weight of Beep?")
    Weight_Beep = float(input())

    print("\nWhat is the weight of Bop?")
    Weight_Bop = float(input())

    print("\nWhat would you like to calcluate (sum or average)?")
    choice = str(input())
    if choice == "sum":
        #Sum = sum_weights(Weight_Beep,Weight_Bop)
        print("\nThe sum of Beep and Bop's weight is ", str(Sum))
    elif choice == "average":
        Avg = calc_avg_weight(Weight_Beep,Weight_Bop)
        print("\nThe average of Beep and Bop's weight is ", str(Avg))
run()

