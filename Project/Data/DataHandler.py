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
        self.numberOfTickers = 15
        self.df = pd.DataFrame()

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

    if __name__== "__main__":
        dh = Datahandler()
        dh.main()
