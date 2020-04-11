import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class MainWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Zoltar Stock Trader Main Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Load Model",
                            command = lambda: controller.toLoadPage())
        button1.pack()

        button2 = tk.Button(self, text = "Train New Model",
                            command = lambda: controller.toNewModel())
        button2.pack()

        button3 = tk.Button(self, text = "Add Model",
                            command = lambda: controller.toAddModel())
        button3.pack()

        button4 = tk.Button(self, text = "Developer Tools",
                            command = lambda: controller.toDevTools())
        button4.pack()




# TODO Settings and Graph Page
#        makeNewModelButton = ttk.Button(self, text="Settings",
#                            command = lambda: controller.showFrame())
#        makeNewModelButton.pack()

#        loadExistingModelButton = ttk.Button(self, text="Graph Page",
#                            command = lambda: controller.showFrame())
#        loadExistingModelButton.pack()

# When Window.py is run then it is assumed the program should run.
