def climb_ladder(steps_crossed, steps_remaining):
    if steps_crossed < steps_remaining:
        print("Still some way to go!")
    else:
        print("We made it!")

climb_ladder(2, 5)
climb_ladder(5, 5)
