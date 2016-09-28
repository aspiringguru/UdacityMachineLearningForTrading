"""
Utility functions
from week 1 quiz 'Utility functions for reading data'
https://classroom.udacity.com/courses/ud501/lessons/3975568860/concepts/41007385930923
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

    df = df.dropna()
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-01-26')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    print df


if __name__ == "__main__":
    test_run()
