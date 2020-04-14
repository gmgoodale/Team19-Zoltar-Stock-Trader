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

    def drawPredictionHistory(self, predictions, stockName, widgetRow):
        widgetCol = 0
        barLabel = tk.Label(self, text = stockName + " Prediction Accuracy Over Time", font = SMALL_FONT)
        barLabel.grid(row = widgetRow, column = widgetCol, columnspan = 10, sticky = tk.S, padx = 5, pady = 5)
        bar = tk.Frame(self)
        for i in range(0, len(predictions)):
            bar.grid_columnconfigure(i, weight = 1)
            if predictions[i] == 1:
                self.drawColoredCell(bar, "green", i)

            else:
                self.drawColoredCell(bar, "red", i)

        bar.grid(row = widgetRow + 1, column = widgetCol, columnspan = 10, sticky = tk.N, padx = 5, pady = 0)

    def drawColoredCell(self,bar, color, col):
        cell = tk.Frame(bar, bg = color)
        cell.grid(column = col, row = 0, padx = 0, pady = 0)
        # Change the background of this to red or green


    #============================ Field Methods ==================================================
    def setModelID(self, modelID):
        self.modelIDText.delete(1.0, "end")
        self.modelIDText.insert("end", modelID)

    def setModelRatio(self, dataFrame, stockNames):
        # Summing True Predictions
        total = 0
        numCorrect = 0
        df = dataFrame.dropna()
        for S in stockNames:
            outcomes = df["Outcome " + S].tolist()
            for outcome in outcomes:
                if (str(outcome) == "True"):
                    numCorrect = numCorrect + 1
                total = total + 1

        self.modelRatioText.delete(1.0, "end")
        ratioString = str(numCorrect) + "/" + str(total)
        self.modelRatioText.insert("end", ratioString)

        row = 2
        for S in stockNames:
            predictions = df["Prediction " + S].tolist()
            self.drawPredictionHistory(predictions, S, row)
            row = row + 2

    def getPredictionHistory(self, dataFrame, stockName):
        return dataFrame["Predictions " + stockName]
