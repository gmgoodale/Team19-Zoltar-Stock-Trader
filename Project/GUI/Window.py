#!/usr/bin/python
import importlib

# Add page files here
import Grapher
import MainPage
import NewPredictionPage
import AddModelPage
import DevToolsPage
import DNNPage

from pathlib import Path

import tkinter as tk
from tkinter import ttk

import pandas
import os

import Model

LARGE_FONT = ("Verdana", 12, "bold")
SMALL_FONT = ("Verdana", 10)

datafolder = Path("Data/Tickers")

# Base of the user interface; calls pages to be used from frames.
class UserInterface(tk.Tk):
    # Easier for reading
    def __init__(self, *args, **kwargs):
        #======================= Creating the window =====================
        super().__init__(*args, **kwargs)

        #tk.Tk.iconbitmap(self, default = "Zoltar_Icon.ico")
        tk.Tk.wm_title(self, "Zoltar")

        # Container = window seen
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_rowconfigure(1, weight = 1)
        container.grid_columnconfigure(0, weight = 3) # Weights the graph to be larger
        container.grid_columnconfigure(1, weight = 1)

        # Frame configuration: loop runs through right-side frames
        self.frames = {}

        # Add all right-side frames to this loop
        for F in (MainPage.MainWindow, NewPredictionPage.NewPredictionWindow, AddModelPage.AddModelWindow,
                  DevToolsPage.DevToolsWindow):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 1, sticky = "nsew")

        frame = DNNPage.DNNWindow(container, self)
        self.frames[DNNPage.DNNWindow] = frame

        frame.grid(row = 1, column = 1, sticky = "nsew")

        # Only 1 Left-side frame, but same function as loop
        frame = Grapher.GrapherWindow(container, self)
        self.frames[Grapher.GrapherWindow] = frame

        frame.grid(row = 0, rowspan = 2, column = 0, sticky = "nsew")

        self.showFrame(MainPage.MainWindow) # Initial page to show

    #====================== Data Handling Methods ======================
    # Needs list: report available csv, append Model Results, get stock name,
    # Get CSV from Stock name
    def saveNewPrediction(self):
        #============================== Collecting Variables ===============================
        frame = self.frames[NewPredictionPage.NewPredictionWindow]

        stockNames = frame.getCurrentlySelectedStocks()
        startDate = frame.getStartDate()
        endDate = frame.getEndDate()
        predictionName = frame.getName()
        predictionWindow = frame.getPredictionWindow()

        print("someting")
        print(predictionWindow)

        path = "Data" + os.sep + "Saved_Stock_Data" + os.sep + predictionName + ".csv"

        #=============================== Generating File ==================================
        allData = pandas.DataFrame()

        for stock in stockNames:
            # Get the stock data from a CSV and put it in a data frame for editing
            stockPath = "Data" + os.sep + "Tickers" + os.sep + stock + "_PriceData_40Years.csv"
            csvData = pandas.read_csv(stockPath)
            # Reanme the thrid colunm to the stock name
            csvData.columns = ["Date", "Open", stock]
            # Get rid of the open column, we just look at close prices
            del csvData["Open"]
            csvData["Date"] = pandas.to_datetime(csvData["Date"])
            csvData = csvData.set_index("Date")
            # The grapher has trouble with large floating numbers so truncate here
            csvData[stock] = csvData[stock].round(decimals = 2)
            # Then add it to the larger dataframe
            allData = pandas.concat([allData, csvData], axis=1, sort=False)

        allData['stockNames'] = stockNames
        # Save the combined, modified, data frames
        allData[startDate:endDate].to_csv(path, mode='a', header = True)


    def getAvailableCSVs(self):
        fileNames = os.listdir("Data" + os.sep + "Saved_Stock_Data")
        return fileNames

    def appendModelResults(self, fileName, modelResults):
        try:
            csvData = pandas.read_csv(fileName)

        except:
            print("ERROR: when reading csv file {}; aborting.".format(fileName))
            return False

        csvData['Model-Prediction'] = modelResults

        try:
            csvData.to_csv(fileName)

        except:
            print("ERROR: when writing to csv file{}; aborting.".format(filename))
            return False

        return True

    def getAvailableStockNames(self):
        stockNames = ["A", "AAP", "ABBV", "ABT", "ACN", "ADBE", "AES", "AET", "AFL",
                                    "AKAM", "ALB", "ALK", "AMD", "AMG", "AOS", "APD",
                                    "ARE", "ATVI", "AYI", "MMM"]
        return stockNames

    def getTickerCSVFromName(self, stockName):
        fileName = stockName + "_PriceData.csv"
        if os.path.isfile(datafolder + "/" + filename):
            return fileName

        print("ERROR: No stock data found for {}".format(filename))


    #====================== DNN Handling Methods =======================
    # Needs List: Load model results, report available models,
    #             Train new DNN

    def getAvailableModels(self):
        modelNames = ["Test Model"]
        return modelNames

    def getModelResults(self, modelName):
        # Test data, unsure how models are run [[time], [up/down]]
        results = [[1, 2, 3, 4,], [0, 0, 1, 1]]
        return results


    #===================== Grapher Interface Methods ========================
    # Needs List:
    def changeGrapherLabel(self, newLabel):
        frame = self.frames[Grapher.GrapherWindow]
        frame.GrapherWindow.changeLabel(newLabel)

    def displayGraph(self, fileName = "TestData.csv"):
        try:
            data = pandas.read_csv("Data" + os.sep + "Saved_Stock_Data" + os.sep + fileName)

        except:
            print("ERROR: when reading csv file {}; aborting.".format(fileName))
            return False

        frame = self.frames[Grapher.GrapherWindow]
        frame.generateGraph(fileName = csvFileName)

        frame = self.frames[DNNPage.DNNWindow]
        frame.setModelRatio(data, stockNames)

    #======================= Navigation Methods ========================
    def showFrame(self, cont):
        try:
            frame = self.frames[cont]

        except:
            return -1
        # raise; all other frames are underneath (Saves state of each)
        frame.tkraise()
        return 0

    def toHome(self):
        self.showFrame(MainPage.MainWindow)

    def toLoadPage(self):
        self.showFrame(LoadPage.LoadWindow)

    def toNewPrediction(self):
        self.showFrame(NewPredictionPage.NewPredictionWindow)

    def toAddModel(self):
        self.showFrame(AddModelPage.AddModelWindow)

    def toDevTools(self):
        self.showFrame(DevToolsPage.DevToolsWindow)


# When Window.py is run then it is assumed the program should run.

zoltar = UserInterface()
zoltar.geometry("1920x1080")
zoltar.mainloop()
