#Kyle Sizemore
#2/7/2020

# pull historical data from the market for backtesting purposes and output to a
# csv file on our mySQL database
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime
import pandas as pd
import pandas_datareader as web
import csv
import pymysql
from sqlalchemy import create_engine
import numpy as np

class Datahandler():

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:pass@127.0.0.1:3306/zoltarpricedata')
        self.start = datetime.datetime(1980,1,1)
        self.end = datetime.datetime.now()
        self.tickers = []
        self.numberOfTickers = 15

    def readTickers():
        with open('TargetTickers.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            tickers.append(row[0])

    def GenYahDataFrame(self, t):
        df = web.DataReader(t, 'yahoo',self.start,self.end)
        return df
        '''
        try:
            df = web.DataReader(t, 'yahoo',start,end)
            return df
        except:
            print('Bad ticker: ' + t)
            return None'''

    def TrimDataFrame(self, df):
        return df.drop(columns = ['High','Low','Volume','Adj Close'])

    def sqlExport(df, t):
        try:
            df.to_sql(t.lower(),con = engine,index = True,index_label='Date',if_exists = 'append',method = None)
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print('Exported ' + t + ' data to SQL')

    def toNumpy(self, endDate, dayInterval, ticker):
        df = self.GenYahDataFrame(ticker)
        df = self.TrimDataFrame(df)

        arr = df.to_numpy()

        numRows = int(np.size(arr,0)/dayInterval)
        outputArr = np.zeros([numRows, dayInterval])

        for i in range(numRows):
            outputArr[i] = np.copy(arr[i*100:((i+1)*100), 1])

        return outputArr

    def main(self):
        end = datetime.datetime.now()
        numpyarray = self.toNumpy(end, 100, 'AOS')
        print(numpyarray)
        print("Size: " + str(np.size(numpyarray)))

if __name__== "__main__":
    dh = Datahandler()
    dh.main()
