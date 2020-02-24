import DataDandler
import import numpy as np

class test_DataHandler:
    DHandler = DataHandler()

    def test_readTickers():
        result = True
        DHandler.readTickers()
        if DHandler.tickers[0] == None:
            result = False
        assert result == True

    def test1_GenYahDataFrame():
        testTicker = 'MMM'
        df = DataHandler.GenYahDataFrame(testTicker)
        if df == None:
            result = False
        assert result == True

    def test2_GenYahDataFrame():
        testTicker = '1234'
        result = True
        df = DataHandler.GenYahDataFrame(testTicker)
        if df != None:
            result = False
        assert result == True

    def test_TrimDataFrame():
        result = True
        DHandler.GenYahDataFrame('MMM')
        TrimDataFrame()
        if len(DHandler.df.columns) != 2:
            result = False
        assert result == True;

    def test_sqlExport():
        result = DHandler.sqlExport('MMM')
        assert result == 'Exported MMM data to SQL';

    def test_toNumpy():
        result = True
        numpyAr = toNumpy(DHandler.end,50,'MMM')
        if numpyAr == None:
            result = False
        assert result == True

    def test_exportTickers():
        result = DHandler.exportTickers()
        assert result == 'Tickers Succesfully Exported';
