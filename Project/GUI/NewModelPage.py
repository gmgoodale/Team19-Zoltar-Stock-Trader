import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)
class NewModelWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New Model", font = LARGE_FONT)
        label.grid(column = 0, columnspan = 3, row = 0, sticky = tk.N,
                   pady = 10)

        #============================= Name Field Code ===============================
        nameFieldLabel = tk.Label(self, text = "Model Name", font = SMALL_FONT)
        nameFieldLabel.grid(column = 0, row = 1, sticky = tk.W, pady = 10, padx = 10)

        newName = tk.StringVar()
        nameField = tk.Entry(self, width = 20, textvariable = newName)
        nameField.grid(column = 1, columnspan = 2, row = 1, padx = 10, pady = 10)

        #============================= ListBox Code ================================
        availableStockLabel = tk.Label(self, text = "Available Stocks", font = SMALL_FONT)
        availableStockLabel.grid(column = 0, row = 2, sticky = tk.S + tk.W, padx = 10, pady = 3)

        availableStocks = controller.getAvailableStockNames()
        selectedStocks = []

        scrollBarforAvailable = tk.Scrollbar(self)
        scrollBarforAvailable.grid(column = 1, row = 3, rowspan = 2, padx = 0, pady = 3)

        self.availableStockListBox = tk.Listbox(self, font = SMALL_FONT, height = 4,
                                                yscrollcommand = scrollBarforAvailable.set)
        scrollBarforAvailable.config(command = self.availableStockListBox.yview)
        for S in availableStocks:
            self.availableStockListBox.insert(tk.END, S)
        self.availableStockListBox.grid(column = 0, row = 3, rowspan = 2, padx = 10, pady = 3)


        #============================ SpinBox Code ==================================
        spinBoxLabel = tk.Label(self, text = "# Days to Analyze", font = SMALL_FONT)
        spinBoxLabel.grid(column = 2, row = 2, sticky = tk.E + tk.S, padx = 10, pady = 3)

        self.spinBox = ttk.Spinbox(self, width = 10, from_ = 0, to = 100)
        self.spinBox.grid(column = 2, row = 3, sticky = tk.E, padx = 10, pady = 3)

        button1 = tk.Button(self, text = "Back To Main Page", font = SMALL_FONT,
                            command = lambda: controller.toHome())
        button1.grid(column = 0, columnspan = 10, row = 10, sticky = tk.N, padx = 10, pady = 20)

    def updateComboBox(self, controller):
        self.selectionBox['values'] = controller.getAvailableModels()
