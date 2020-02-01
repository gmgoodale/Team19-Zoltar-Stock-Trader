#Kyle Sizemore
#1/31/2020

#pull historical data from the market for backtesting purposes and output to a file.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import datetime
import pandas as pd
import pandas_datareader.data as web



start = datetime.datetime(2019,1,1)
end = datetime.datetime(2019,5,31)
df_500 = web.DataReader('^GSPC', 'yahoo',start,end)
df_500.tail()
print (df_500[:5])

#import sys
#for p in sys.path:
#    print(p)
