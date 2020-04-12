#Kyle Sizemore
#2/7/2020

# pull historical data from the market for backtesting purposes and output to a
# csv file in our repository
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime
import pandas as pd
import pandas_datareader as web
import csv
import pymysql
from sqlalchemy import create_engine
import numpy as np

class DataHandler:

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:pass@127.0.0.1:3306/zoltarpricedata')
        self.start = datetime.datetime(1980,1,1)
        self.end = datetime.datetime.now()
        self.tickers = []
        self.numberOfTickers = 20
        self.df = pd.DataFrame()

    def setTimeframe(start,end):
        if type(start) is datetime and type(end) is datetime:
            self.start = start
            self.end = end

    def readTickers(self):
        with open('TargetTickers.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.tickers.append(row[0])

    def GenYahDataFrame(self,t):
        try:
            self.df = web.DataReader(t, 'yahoo',self.start,self.end)

        except:
            print('Bad ticker: ' + t)
            self.df = pd.DataFrame()

    def TrimDataFrame(self):
        self.df.drop(columns = ['High','Low','Volume','Adj Close'])

    def sqlExport(t):
        try:
            df.to_sql(t.lower(),con = engine,index = True,index_label='Date',if_exists = 'append',method = None)
        except ValueError as vx:
            return (vx)
        except Exception as ex:
            return (ex)
        else:
            return ('Exported ' + t + ' data to SQL')

    # This takes the data frame and creates a numpy array. The numpy array is
    # 2-D with the number of rows being the datapoints/dayInterval and the row
    # width being the dayIntercal. EX: toNumpy(currentDate, 100, AOS) returns
    # a numpy array of size (91, 100) because it has at least 9100 days of
    # history and 100 is the interval of interest
    def toNumpy(self, endDate, dayInterval, ticker):
        df = self.GenYahDataFrame(ticker)
        df = self.TrimDataFrame(df)

        arr = df.to_numpy()

        numRows = int(np.size(arr,0)/dayInterval)
        outputArr = np.zeros([numRows, dayInterval])

        for i in range(numRows):
            outputArr[i] = np.copy(arr[i*100:((i+1)*100), 1])

        return outputArr

    def exportTickers(self):
        for t in self.tickers[:self.numberOfTickers]:
            self.GenYahDataFrame(t)
            if not self.df.empty:
                self.TrimDataFrame()
                self.csvExport(t)
            self.numberOfTickers = self.numberOfTickers + 1;
        return('Tickers Succesfully Exported')

    def csvExport(self,ticker):
        #start = self.start.strftime("%m/%d/%Y")
        #end = self.end.strftime("%m/%d/%Y")
        #timeInterval = start + '-' + end
        self.df.to_csv('Tickers/'+ ticker + '_PriceData_40Years')
        return ('Exported ' + ticker + ' data to CSV file')

if __name__== "__main__":
    dh = DataHandler()
    dh.readTickers()
    dh.exportTickers()
