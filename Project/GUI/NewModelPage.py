import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class NewModelWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="New Model", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Back To Main Page",
                            command = lambda: controller.toHome())
        button1.pack()
