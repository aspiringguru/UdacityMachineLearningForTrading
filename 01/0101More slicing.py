"""
Utility functions
from week 1 quiz 'More slicing'
https://classroom.udacity.com/courses/ud501/lessons/3975568860/concepts/41007385960923
"""
import os
import pandas as pd


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """
    Read stock data (adjusted close) for given symbols from CSV files.
    date = range of dates
    """
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna()
            #drop rows where SPY did not trade.
            #NB this is different from dropping any row with NaN in it.
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    #slice by row range (dates) using DataFrame
    #print df.ix['2010-01-01':'2010-01-15']#month of January
    #http://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.DataFrame.ix.html
    print "GOOG\n", df['GOOG'].head(4)
    print "GOOG\n", df[['GOOG', 'SPY']].head(4)
    print "slice by date range '2010-01-01':'2010-01-15' and stocks 'GOOG', 'SPY' "
    print df.ix['2010-01-01':'2010-01-15', ['GOOG', 'SPY']]


if __name__ == "__main__":
    test_run()


#http://pandas.pydata.org/pandas-docs/stable/indexing.html
