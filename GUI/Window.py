#!/usr/bin/python

from tkinter import *

class UserInterface:
    def new_window(self):
        window = Tk()
        window.title("ZOLTAR")
        window.geometry('800x400')

        lbl = Label(window, text = "ZOLTAR: TELLER AND BRINGER OF FORTUNES!!")
        lbl.grid(column = 0, row = 1)

        def response():
            lbl.configure(text = "HA. ZOLTAR HAS FOOLED YOU!")
        btn = Button(window, text = "THIS BUTTON DOES NOTHING", command = response)
        btn.grid(column = 2, row = 2)

        window.mainloop()

testCase = UserInterface()
testCase.new_window()
