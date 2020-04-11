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

        self.comboBoxSelection = tk.StringVar()
        self.selectionBox = ttk.Combobox(self, width = 20, textvariable = self.comboBoxSelection)
        self.selectionBox['postcommand'] = self.updateComboBox(controller)
        self.selectionBox.pack()

        loadButton = tk.Button(self, text = "Load Graph",
                               command = lambda: controller.displayGraph(csvFileName = self.selectionBox.get()))

        loadButton.pack()

    def updateComboBox(self, controller):
        self.selectionBox['values'] = controller.getAvailableCSVs()
