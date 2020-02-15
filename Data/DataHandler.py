#Kyle Sizemore
#2/7/2020

# pull historical data from the market for backtesting purposes and output to a
# csv file on our mySQL database
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime
import pandas as pd
import pandas_datareader.data as web
import csv
import pymysql
from sqlalchemy import create_engine

class Datahandler:
    engine = create_engine('mysql+pymysql://root:pass@127.0.0.1:3306/zoltarpricedata')
    start = datetime.datetime(1980,1,1)
    end = datetime.datetime.now()
    tickers = []
    numberOfTickers = 15

    def __init__(self):
        self.unitTests()
    def readTickers():
        with open('TargetTickers.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            tickers.append(row[0])

    def GenYahDataFrame(t):
        try:
            df = web.DataReader(t, 'yahoo',start,end)
            return df
        except:
            print('Bad ticker: ' + t)
            return None

    def TrimDataFrame(df):
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

    def unitTests():
        for t in tickers[:numberOfTickers]:
            df = GenYahDataFrame(t)
            if df != None:
                df = TrimDataFrame(df)
                sqlExport(df, t)
        print('Tickers Succesfully Exported')
