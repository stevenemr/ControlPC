from tkinter import *
import mousecontrol as mc

view = Tk()
view.title("ControlPC")

appTitle = Label(text="ControlPC",
                 font=("Arial", 26))
appTitle.pack()

mouseimg = PhotoImage(file="img/mouse.png")

moveButton = Button(command=mc.func,
                    image=mouseimg)
moveButton.pack()

view.mainloop()