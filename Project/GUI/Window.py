#!/usr/bin/python
import importlib
import Window

from tkinter import *

# Class containing the high level calls required to run a UI
class UserInterface:

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default = "clienticon.ico")
        tk.Tk.wm_title(self, "Zoltar")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (GrapherWindow):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(GrapherWindow)

    # Attempts to show a frame given a container 'cont'
    # Success returns 0, failure returns -1
    def show_frame(self, cont):
        try:
            frame = self.frames[cont]

        except:
            return -1

        frame.tkraise()
        return 0

    # Creates a new window of the Zoltar application on the menu screen
    def newWindow(self):
        window = Tk()
        window.title("ZOLTAR")
        window.geometry('800x400')

        self.drawMenu(window)

        window.mainloop()

    # Draws the initial menu on screen
    def drawMenu(self, window):
        lbl = Label(window, text = "ZOLTAR: TELLER AND BRINGER OF FORTUNES!!")
        lbl.grid(column = 0, row = 1)

        def response():
            lbl.configure(text = "HA. ZOLTAR HAS FOOLED YOU!")

        btn = Button(window, text = "THIS BUTTON DOES NOTHING", command = response)
        btn.grid(column = 2, row = 2)


class UserInterfaceTester:

    def __init__(self):
        subject = UserInterface()
        self.runTestBattery()

    def runTestBattery(self):
        self.test_newWindow()

    def test_newWindow(self):
        subject.newWindow()
        
