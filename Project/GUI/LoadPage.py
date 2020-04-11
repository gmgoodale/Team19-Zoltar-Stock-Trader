import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class LoadWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Load Model", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Back To Main Page",
                            command = lambda: controller.toHome())
        button1.pack()

        loadButton = tk.Button(self, text = "Load Graph",
                               command = lambda: controller.displayGraph())

        '''
        comboBoxSelection = tk.StringVar()
        selectionBox = ttk.Combobox(self, width = 20, textvariable = comboBoxSelection)
        selectionBox['values'] = controller.modelList
        comboBoxSelection.pack()
        '''
