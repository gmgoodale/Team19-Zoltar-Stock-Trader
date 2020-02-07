#Kyle Sizemore
#2/7/2020

#pull historical data from the market for backtesting purposes and output to a file.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime
import pandas as pd
import pandas_datareader.data as web
import csv

start = datetime.datetime(1980,1,1)
end = datetime.datetime.now()
tickers = []
with open('TargetTickers.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        tickers.append(row[0])
for t in tickers[:25]:
    try:
        df = web.DataReader(t, 'yahoo',start,end)
        print('Exporting ' + t + ' data to csv...')
        df[['Open','Close']].iloc[:].to_csv('Tickers/' + t+'_PriceData_Long.csv')
    except:
        print('Bad ticker: ' + t)
        pass
print(t + ' Exported successfully')

#print (df[['Open','Close']].iloc[:])
