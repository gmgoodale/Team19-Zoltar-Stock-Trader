import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class LoadWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure(0, weight = 1)

        label = tk.Label(self, text = "Load Model", font = LARGE_FONT)
        label.grid(column = 0, columnspan = 10, row = 0, padx = 10, pady = 20, sticky = tk.N)

        self.drawComboBox(parent, controller)

        loadButton = tk.Button(self, text = "Load Model",
                               command = lambda: controller.displayGraph(csvFileName = self.selectionBox.get()))
        loadButton.grid(column = 0, row = 2, padx = 10, pady = 10, sticky = tk.N)

        toHomeButton = tk.Button(self, text = "Back To Main Page",
                            command = lambda: controller.toHome())
        toHomeButton.grid(column = 0, columnspan = 10, row = 10, padx = 10, pady = 20, sticky = tk.S)



    def drawComboBox(self, parent, controller):
        self.comboBoxSelection = tk.StringVar()
        self.selectionBox = ttk.Combobox(self, width = 20, textvariable = self.comboBoxSelection)
        self.selectionBox['postcommand'] = self.updateComboBox(controller)
        self.selectionBox.grid(column = 0, row = 1, padx = 10, pady = 10, sticky = tk.N)

    def updateComboBox(self, controller):
        self.selectionBox['values'] = controller.getAvailableCSVs()
