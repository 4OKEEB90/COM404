from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=0)
    # style
        self.heading_label.configure(font="Arial 20", text="Entrance Ticket")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=2, column=0, sticky=W)
    # style
        self.instruction_label.configure(font="Arial 10", text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        self.ticket_entry = Entry()
        self.ticket_entry.grid(row=3,column=0)
        
    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=4,column=0)
    #style
        self.buy_button.configure(font="Arial 10", text="Buy")