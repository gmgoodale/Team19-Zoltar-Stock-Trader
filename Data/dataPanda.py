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

# 40 years back
start = datetime.datetime(1980,1,1)
end = datetime.datetime.now()
tickers = []
numberOfTickers = 15
with open('TargetTickers.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        tickers.append(row[0])
for t in tickers[:numberOfTickers]:
    try:
        df = web.DataReader(t, 'yahoo',start,end)
        print('Exporting ' + t + ' data to csv...')
        df[['Open','Close']].iloc[:].to_csv('Tickers/' + t+'_PriceData_Long.csv')
        print(t + ' Exported successfully')
    except:
        print('Bad ticker: ' + t)
        numberOfTickers += 1
        pass
print('Tickers Succesfully Exported')

#print (df[['Open','Close']].iloc[:])
