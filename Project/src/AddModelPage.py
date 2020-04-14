import importlib

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12, "bold")
SMALL_FONT = ("Verdana", 10)

class AddModelWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_rowconfigure(10, weight = 1)

        label = tk.Label(self, text="New Model", font = LARGE_FONT)
        label.grid(column = 0, columnspan = 3, row = 0, sticky = tk.N,
                   pady = 10)

        self.drawNameField(parent, controller, 1, 0)
        self.drawAvailableListBox(parent, controller, 2, 0)
        self.drawSaveButton(parent, controller, 5, 0)
        self.drawToHomeButton(parent, controller, 10, 0)

    #========================================== Draw Methods =======================================
    def drawNameField(self, parent, controller, row, col):
        nameFieldLabel = tk.Label(self, text = "Model Name", font = SMALL_FONT)
        nameFieldLabel.grid(column = col, row = row, sticky = tk.W, pady = 10, padx = 10)

        newName = tk.StringVar()
        self.nameField = tk.Entry(self, width = 20, textvariable = newName, font = SMALL_FONT,)
        self.nameField.grid(column = col + 1, columnspan = 2, row = row, padx = 10, pady = 10, sticky = tk.W)

    def drawAvailableListBox(self, parent, controller, row, col):
        availableStockLabel = tk.Label(self, text = "Available Stocks", font = SMALL_FONT)
        availableStockLabel.grid(column = col, row = row, sticky = tk.S + tk.W, padx = 10, pady = 3)

        availableStocks = controller.getAvailableStockNames()

        scrollBarforAvailable = tk.Scrollbar(self)
        scrollBarforAvailable.grid(column = col + 1, row = row + 1, rowspan = 2, padx = 0, pady = 3, sticky = tk.W)

        self.availableStockListBox = tk.Listbox(self, font = SMALL_FONT, height = 6,
                                                yscrollcommand = scrollBarforAvailable.set)
        self.availableStockListBox.grid(column = col, row = row + 1, rowspan = 2, padx = 0, pady = 3)

        scrollBarforAvailable.config(command = self.availableStockListBox.yview)

        for S in availableStocks:
            self.availableStockListBox.insert(tk.END, S)

    def drawSaveButton(self, parent, controller, row, col):
        saveButton = tk.Button(self, text = "Save New Model", font = SMALL_FONT)
        saveButton.grid(column = col, columnspan = 10, row = row, padx = 5, pady = 10)
    def drawToHomeButton(self, parent, controller, row, col):
        toHomeButton = tk.Button(self, text = "Back To Main Page", font = SMALL_FONT,
                            command = lambda: controller.toHome())
        toHomeButton.grid(column = col, columnspan = 10, row = row, padx = 5, pady = 20)
