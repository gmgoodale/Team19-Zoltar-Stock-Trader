#!/usr/bin/python
import importlib
import Window

from tkinter import *

# Base of the user interface; calls pages to be used from frames.
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

        self.show_frame(StartPage, GrapherWindow)

    # Attempts to show a frame given a container 'cont'
    # Success returns 0, failure returns -1
    def show_frame(self, cont):
        try:
            frame = self.frames[cont]

        except:
            return -1

        frame.tkraise()
        return 0

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Zoltar Stock Trader Main Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        grapherButton = ttk.Button(self, text = "grapher",
                            command=lambda: controller.show_frame(PageOne))
        grapherButton.pack()

        makeNewModelButton = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        makeNewModelButton.pack()

        loadExistingModelButton = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        loadExistingModelButton.pack()

# When Window.py is run then it is assumed the program should run.
zoltar = UserInterface()
zoltar.mainloop()
