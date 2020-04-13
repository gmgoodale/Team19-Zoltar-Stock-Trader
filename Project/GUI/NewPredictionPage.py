import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

LARGE_FONT = ("Verdana", 12, "bold")
SMALL_FONT = ("Verdana", 10)
class NewPredictionWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(2, weight = 1)

        label = tk.Label(self, text="New Prediction", font = LARGE_FONT)
        label.grid(column = 0, columnspan = 3, row = 0, sticky = tk.N,
                   pady = 10)

        self.drawNameField(parent, controller)
        self.drawAvailableListBox(parent, controller)
        self.drawSelectedListBox(parent, controller)
        self.drawSpinBox(parent, controller)
        self.drawIntitialDateEntry(parent, controller)
        self.drawEndDateEntry(parent, controller)

        saveButton = tk.Button(self, text = "Save Prediction", font = SMALL_FONT,
                               command = lambda: controller.saveNewPrediction())
        saveButton.grid(column = 2, columnspan = 10, row = 7, sticky = tk.N, padx = 10, pady = 20)

        button1 = tk.Button(self, text = "Back To Main Page", font = SMALL_FONT,
                            command = lambda: controller.toHome())
        button1.grid(column = 0, columnspan = 10, row = 10, sticky = tk.S, padx = 10, pady = 20)

    #======================================= Draw Functions ========================================
    def drawNameField(self, parent, controller):
        nameFieldLabel = tk.Label(self, text = "Prediction Name", font = SMALL_FONT)
        nameFieldLabel.grid(column = 0, row = 1, sticky = tk.W, pady = 10, padx = 10)

        newName = tk.StringVar()
        self.nameField = tk.Entry(self, width = 20, textvariable = newName, font = SMALL_FONT,)
        self.nameField.grid(column = 1, columnspan = 2, row = 1, padx = 10, pady = 10, sticky = tk.W)

    def drawAvailableListBox(self, parent, controller):
        availableStockLabel = tk.Label(self, text = "Available Stocks", font = SMALL_FONT)
        availableStockLabel.grid(column = 0, row = 2, sticky = tk.S + tk.W, padx = 10, pady = 3)

        availableStocks = controller.getAvailableStockNames()

        scrollBarforAvailable = tk.Scrollbar(self)
        scrollBarforAvailable.grid(column = 1, row = 3, rowspan = 2, padx = 0, pady = 3, sticky = tk.W)

        self.availableStockListBox = tk.Listbox(self, font = SMALL_FONT, height = 6,
                                                yscrollcommand = scrollBarforAvailable.set)
        self.availableStockListBox.grid(column = 0, row = 3, rowspan = 2, padx = 0, pady = 3)
        self.availableStockListBox.bind('<Double-Button-1>', self.selectStock)

        scrollBarforAvailable.config(command = self.availableStockListBox.yview)

        for S in availableStocks:
            self.availableStockListBox.insert(tk.END, S)


    def drawSelectedListBox(self, parent, controller):
        selectedStockLabel = tk.Label(self, text = "Selected Stocks", font = SMALL_FONT)
        selectedStockLabel.grid(column = 0, row = 5, sticky = tk.S + tk.W, padx = 10, pady = 3)

        scrollBarforSelected = tk.Scrollbar(self)
        scrollBarforSelected.grid(column = 1, row = 6, rowspan = 2, padx = 0, pady = 3, sticky = tk.W)

        self.selectedStockListBox = tk.Listbox(self, font = SMALL_FONT, height = 4,
                                                yscrollcommand = scrollBarforSelected.set)
        self.selectedStockListBox.grid(column = 0, row = 6, rowspan = 2, padx = 0, pady = 3)
        self.selectedStockListBox.bind('<Double-Button-1>', self.deselectStock)

        scrollBarforSelected.config(command = self.selectedStockListBox.yview)

    def drawSpinBox(self, parent, controller):
        spinBoxLabel = tk.Label(self, text = "# Days to Analyze", font = SMALL_FONT)
        spinBoxLabel.grid(column = 2, row = 2, sticky = tk.E + tk.S, padx = 10, pady = 3)

        self.spinBox = ttk.Spinbox(self, width = 10, from_ = 0, to = 100)
        self.spinBox.grid(column = 2, row = 3, sticky = tk.E, padx = 10, pady = 3)

    def drawIntitialDateEntry(self, parent, controller):
        widgetRow = 8
        widgetCol = 0

        initialDateLabel = tk.Label(self, text = "Initial Date", font = SMALL_FONT)
        initialDateLabel.grid(column = widgetCol, row = widgetRow, sticky = tk.S, padx = 10, pady = 3)

        self.initialDateEntry = DateEntry(self, width = 10, borderwidth = 2)
        self.initialDateEntry.grid(column = widgetCol, row = widgetRow + 1, padx = 10, pady = 3)


    def drawEndDateEntry(self, parent, controller):
        widgetRow = 8
        widgetCol = 2

        endDateLabel = tk.Label(self, text = "End Date", font = SMALL_FONT)
        endDateLabel.grid(column = widgetCol, row = widgetRow, sticky = tk.S, padx = 10, pady = 3)

        self.endDateEntry = DateEntry(self, width = 10, borderwidth = 2)
        self.endDateEntry.grid(column = widgetCol, row = widgetRow + 1, padx = 10, pady = 3)


    #======================================= Frame Functions =======================================
    def updateComboBox(self, controller):
        self.selectionBox['values'] = controller.getAvailableModels()

    def selectStock(self, event):
        try:
            index = self.availableStockListBox.curselection()[0]
            name = self.availableStockListBox.get(index)
            self.selectedStockListBox.insert(tk.END, name)
            self.availableStockListBox.delete(index)

        except:
            return

    def deselectStock(self, event):
        try:
            index = self.selectedStockListBox.curselection()[0]
            name = self.selectedStockListBox.get(index)
            self.availableStockListBox.insert(tk.END, name)
            self.selectedStockListBox.delete(index)
        except:
            return

    def getCurrentlySelectedStocks(self):
        return list(self.selectedStockListBox.get(0, tk.END))

    def getStartDate(self):
        return self.initialDateEntry.get_date()

    def getEndDate(self):
        return self.endDateEntry.get_date()

    def getName(self):
        return self.nameField.get()

    def savePrediction(self):
        # grabs the selected stocks to a list
        stockNames = list(self.selectedStockListBox.get(0, tk.END))
        startDate = self.getStartDate()
        endDate = self.getEndDate()
        daysToAnalyze = self.spinBox.get()

        return

class Prediction():
    __init__(startDate, endDate, stockNames, modelPredictions, daysToAnalyze):
        self.stardDate = startDate
        self.endDate = endDate
        self.stockNames = stockNames
        self.daysToAnalyze = daysToAnalyze

    def addModelPredictions(self, modelOut):
        self.modelOut = modelOut
