"""
this code originally by gill.moni.
https://discussions.udacity.com/t/stock-data-in-csv/157369/4
minor mods for usability by AspiringGuru
NB: can also retrieve stock data from google finance. See my other repos here on github.
"""
import urllib
import os 

def fetch_data(symbol): #Not in course. Adding (mgill)
    """ Downloads .csv files for <symbols> from Yahoo Finance and saves them in 'data' directory. These are later picked up by rese of the program."""
    
    '''
    url = "http://ichart.finance.yahoo.com/table.csv?s="+symbol+\
    "&amp;d=1&amp;e=1&amp;f=2016&amp;g=d&amp;a=8&amp;b=7&amp;c=2000&amp;ignore=.csv"
    '''
    
    time_frame = "m" # d -> daily, w -> weekly, m -> monthly.
    url = "http://real-chart.finance.yahoo.com/table.csv?s="+symbol+\
            "&a=11&b=22&c=1998&d=04&e=9&f=2016&g="+time_frame+"+&ignore=.csv"

    fileName = './data/{}.csv'.format(symbol)
    if not os.path.isfile(fileName):
        open(fileName, 'a').close()
        #if fileName does not exist, creates empty file for appending to & close file immediately.
    urllib.urlretrieve(url, fileName)
    print "DEBUG: Downloading for "+symbol
    print "DEBUG: URL:"+url

"""
def test_run():
    # Choose stock symbols to read
    #symbols = ['XLY', 'XLF','XLU','XLP','XLE','XLV','XLB','XLK','XLI']
    symbols = ['AAPL', 'SPY', 'IBM']
    for symbol in symbols:
       fetch_data(symbol) #Download csv for symbol loading.

test_run()
"""
#fetch_data("GOOG")
fetch_data("GLD")