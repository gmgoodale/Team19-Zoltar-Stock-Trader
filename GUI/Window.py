#!/usr/bin/python

from tkinter import *

# Class containing the high level calls required to run a UI
class UserInterface:
    # Creates a new window of the Zoltar application on the menu screen
    def new_window(self):
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

# Test Case to create a new window: passed if the window displays on screen
def uiTest():
    testCase = UserInterface()
    testCase.new_window()

uiTest()
