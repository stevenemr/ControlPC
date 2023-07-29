import mousecontrol as mc
from tkinter import *

view = Tk.tk()
view.title("ControlPC")

appTitle = Label(text="ControlPC",
                 font=("Arial", 26))
appTitle.pack()

startstop = Button(text="Start / Stop")
startstop.pack()

view.mainloop() 