#Kyle Sizemore
#2/7/2020

# pull historical data from the market for backtesting purposes and output to a
# csv file in our repository
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime
import pandas as pd
import pandas_datareader.data as web
import csv
import pymysql
from sqlalchemy import create_engine
import import numpy as np

class DataHandler:
    engine = create_engine('mysql+pymysql://root:pass@127.0.0.1:3306/zoltarpricedata')
    start = datetime.datetime(1980,1,1)
    end = datetime.datetime.now()
    tickers = []
    numberOfTickers = 15
    df = pd.DataFrame()

    def __init__(self):
        self.exportTickers()

    def setTimeframe(start,end):
        if type(start) is datetime and type(end) is datetime:
            self.start = start
            self.end = end

    def readTickers():
        with open('TargetTickers.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            tickers.append(row[0])

    def GenYahDataFrame(t):
        try:
            df = web.DataReader(t, 'yahoo',start,end)

        except:
            print('Bad ticker: ' + t)
            df = None

    def TrimDataFrame():
        df = df.drop(columns = ['High','Low','Volume','Adj Close'])

    def sqlExport(t):
        try:
            df.to_sql(t.lower(),con = engine,index = True,index_label='Date',if_exists = 'append',method = None)
        except ValueError as vx:
            return (vx)
        except Exception as ex:
            return (ex)
        else:
            return ('Exported ' + t + ' data to SQL')

    def toNumpy(self, endDate, dayInterval, ticker):
        df = self.GenYahDataFrame(ticker)
        df = self.TrimDataFrame(df)

        arr = df.to_numpy()

        numRows = int(np.size(arr,0)/dayInterval)
        outputArr = np.zeros([numRows, dayInterval])

        for i in range(numRows):
            outputArr[i] = np.copy(arr[i*100:((i+1)*100), 1])

        return outputArr

    def exportTickers():
        for t in tickers[:numberOfTickers]:
            GenYahDataFrame(t)
            if df != None:
                TrimDataFrame(df)
                cveExport(df,t)
        return('Tickers Succesfully Exported')

    def csvExport(dFrame,ticker):
        timeInterval = start + 'to' + end
        df.to_csv('Tickers/'+ ticker + '_PriceData_' + timeInterval)
        return ('Exported ' + ticker + ' data to CSV file')
