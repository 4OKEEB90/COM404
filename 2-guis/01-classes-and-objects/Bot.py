class Bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("*"*(len(self.name)+2))
        print("*"+str(self.name)+"*")
        print("*"*(len(self.name)+2))

    def display_age(self):
        print("    iiiiiiiiiii   ")
        print("   |:H:a:p:p:y:|  ")
        print(" __|___________|__")
        print("|^^^^^^^^^^^^^^^^^|")
        print("|:B:i:r:t:h:d:a:y:|")
        print("|       "+str(self.age)+"        |")
        print("~~~~~~~~~~~~~~~~~~~")

    def display_energy(self):
        print ("♦"*(self.energy))

    def display_shield(self):
        print("  ____  ")
        print("/_    _\ ")
        print("|_ "+str(self.shield)+" _|")
        print(" \    /")
        print("  \__/  ")

    def display_summary(self):
        print("Name: "+str(self.name))
        print("Age: "+str(self.age))
        print("Energy: "+"♦"*(self.energy))
        print("Shield: "+"0"*(self.shield))

    def __str__(self):
        string = ("{} is {} years old, has {} energy and a shield value of {}".format(self.name, self.age, self.energy, self.shield))
        return string

ben = Bot("Ben", 25, 10, 20)

ben.display_name()
ben.display_age()
ben.display_energy()
ben.display_shield()
ben.display_summary()
print(ben.__str__())

