from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:/Documents/ambulance.gif")
        self.bike_image = PhotoImage(file="U:/Documents/bike.gif")
        self.plane_image = PhotoImage(file="U:/Documents/plane.gif")

        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=1)
        self.heading_label.configure(text="Transport")
    
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image, height=60, width=60)

    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image, height=60, width=60)
 
    def add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image, height=60, width=60)