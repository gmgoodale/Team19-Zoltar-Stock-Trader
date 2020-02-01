#Kyle Sizemore
#1/31/2020

#pull historical data from the market for backtesting purposes and output to a file.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime
import pandas as pd
import pandas_datareader.data as web

start = datetime.datetime(2019,1,1)
end = datetime.datetime.now()
ticker = 'SPCE'
df = web.DataReader(ticker, 'yahoo',start,end)
print('Exporting ' + ticker + ' data to csv...')
df[['Open','Close']].iloc[:].to_csv('Tickers/' + ticker+'_PriceData.csv')
print(ticker + ' Exported successfully')

#print (df[['Open','Close']].iloc[:])
