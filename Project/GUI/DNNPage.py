#!/usr/bin/python
from pathlib import Path

import tkinter as tk
from tkinter import ttk

import pandas

LARGE_FONT = ("Verdana", 12, "bold")
SMALL_FONT = ("Verdana", 10)

class DNNWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)

        windowLabel = tk.Label(self, text = "DNN Statistics", font = LARGE_FONT)
        windowLabel.grid(row = 0, column = 0, columnspan = 10, sticky = tk.N, padx = 10, pady = 20)

        self.drawModelID(parent, controller)
        self.drawModelRatio(parent, controller)
#======================================== Draw Methods =============================================
    def drawModelID(self, parent, controller):
        widgetRow = 1
        widgetCol = 0

        modelIDLabel = tk.Label(self, text = "Current Model:  ", font = SMALL_FONT)
        modelIDLabel.grid(row = widgetRow, column = widgetCol, sticky = tk.W, padx = 2, pady = 5)

        self.modelIDText = tk.Text(self, height = 1, width = 15)
        self.modelIDText.grid(row = widgetRow, column = widgetCol + 1, sticky = tk.W, padx = 2, pady = 5)

    def drawModelRatio(self, parent, controller):
        widgetRow = 2
        widgetCol = 0

        modelRatioLabel = tk.Label(self, text = "Model Accuracy:  ", font = SMALL_FONT)
        modelRatioLabel.grid(row = widgetRow, column = widgetCol, sticky = tk.W, padx = 2, pady = 5)

        self.modelRatioText = tk.Text(self, height = 1, width = 7)
        self.modelRatioText.grid(row = widgetRow, column = widgetCol + 1, sticky = tk.W, padx = 2,
                                 pady = 5)

    def drawPredictionHistory(self, modelHistory, total):
        widgetRow = 2
        widgetCol = 0

        bar = tk.Frame(self)
        for i in range(0, total):
            bar.grid_columnconfigure(i, weight = 1)
            if modelHistory[i] == 1:
                drawColoredCell(bar, green)

            else:
                drawColoredCell(bar, red)

    def drawColoredCell(bar, color):
        cell = tk.Frame(bar)
        # Change the background of this to red or green


    #============================ Field Methods ==================================================
    def setModelID(self, modelID):
        self.modelIDText.delete(1.0, END)
        self.modelIDText.insert(END, modelID)

    def setModelRatio(self, dataFrame, stockNames):
        # Summing True Predictions
        total = stockNames.len() * self.getPredictionResults(dataFrame, stockNames[0]).len() # Stocks * (Pre / Stocks)
        numCorrect = 0
        for S in stockNames:
            for Prediction in self.getPredictionResults(S):
                if bool(Prediction):
                    numCorrect += 1

        self.modelRatioText.delete(1.0, END)
        ratioString = str(numCorrect) + "/" + str(total)
        self.modelRatioText.insert(END, ratioString)

        for S in stockNames:
            modelPredictions =
            self.drawPredictionHistory(modelHistory, total)

    def getPredictionHistory(dataFrame, stockName):
        return dataFrame["Predictions " + stockName]

    def getPredictionResults(dataFrame, stockName):
        return dataFrame["Correct " + stockName]

    def getModelForStock(self, stockName):
