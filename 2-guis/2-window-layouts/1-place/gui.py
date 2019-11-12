from tkinter import *

class Gui(Tk):

    # initialise the window
  def __init__(self):
    super().__init__()

    self.add_heading_label()
    self.add_title()
    self.add_body1_label()
    self.add_body2_label()
    self.add_email_entry()
    self.add_sub_button()
    self.add_

  def add_title(self):
    # create
    self.title("Newsletter")
    #style
    self.configure(bg="#eee", height=175, width=335)

  def add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.place(x=25,y=20)
    # style
    self.heading_label.configure(font="Arial 15", text="RECEIVE OUR NEWSLETTER")

  def add_body1_label(self):
    #create
    self.body1_label = Label()
    self.body1_label.place(x=15,y=70)
    # style
    self.body1_label.configure(font="Arial 9", text="Please enter your email below to receive our newsletter.")
    # handle events
    # (callback functions to handle events will go here)

  def add_body2_label(self):
    #create
    self.body2_label = Label()
    self.body2_label.place(x=20,y=110)
    # style
    self.body2_label.configure(font="Arial 9", text="Email:")
    # handle events
    # (callback functions to handle events will go here)

  def add_email_entry(self):
    #create
    self.email_entry = Entry()
    self.email_entry.place(x=80,y=110)

  def add_sub_button(self):
    #create
    self.sub_button = Button(bg="LightPink1")
    self.sub_button.place(x=10,y=140)
    #style
    self.sub_button.configure(font="Arial 9", text="Subscribe", width = 42)


    
    