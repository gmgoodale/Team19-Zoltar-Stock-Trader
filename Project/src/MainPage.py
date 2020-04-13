import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12, "bold")
SMALL_FONT = ("Verdana", 10)

class MainWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.grid_columnconfigure(0, weight = 1)

        label = tk.Label(self, text="Zoltar Stock Trader Main Page", font = LARGE_FONT)
        label.grid(column = 0, row = 0, pady = 20, padx = 10)

        loadButton = tk.Button(self, text = "Load to Graph", font = SMALL_FONT,
                               command = lambda: controller.displayGraph(fileName = self.selectionBox.get()))
        loadButton.grid(column = 0, row = 3, pady = 5)

        self.drawComboBox(parent, controller)

        toNewModelButton = tk.Button(self, text = "Add Prediction", font = SMALL_FONT,
                            command = lambda: controller.toNewPrediction())
        toNewModelButton.grid(column = 0, row = 4, pady = 20)

        toAddModelButton = tk.Button(self, text = "Train New Model", font = SMALL_FONT,
                            command = lambda: controller.toAddModel())
        toAddModelButton.grid(column = 0, row = 5, pady = 10)

        toDevToolsButton = tk.Button(self, text = "Developer Tools", font = SMALL_FONT,
                            command = lambda: controller.toDevTools())
        toDevToolsButton.grid(column = 0, row = 6, pady = 50)

    def updateComboBox(self, controller):
        self.selectionBox['values'] = controller.getAvailableCSVs()

    def drawComboBox(self, parent, controller):
        comboBoxLabel = tk.Label(self, text = "Available Predictions", font = SMALL_FONT)
        comboBoxLabel.grid(column = 0, row = 1, padx = 10, pady = 0)
        self.comboBoxSelection = tk.StringVar()
        self.selectionBox = ttk.Combobox(self, width = 20, textvariable = self.comboBoxSelection)
        self.selectionBox['postcommand'] = self.updateComboBox(controller)
        self.selectionBox.grid(column = 0, row = 2, padx = 10, pady = 0, sticky = tk.N)
