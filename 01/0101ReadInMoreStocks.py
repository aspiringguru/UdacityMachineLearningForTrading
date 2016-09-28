"""


"""

import pandas as pd
import matplotlib.pyplot as plt

start_date = '2010-01-22'
end_date = '2010-01-26'
dates = pd.date_range(start_date, end_date)
df1 = pd.DataFrame(index=dates)
print "aa__type(df1)=", type(df1), "df1.shape=", df1.shape
#NB: df1 shape is 5 rows & zero columns at this point, but content = []
print "df1=\n", df1
print "df1.columns.values.tolist()=", df1.columns.values.tolist()
#print "index values = df1.index.values=", df1.index.values
#at this stage df1 is an empty dataframe with index values dates in the range between start_date, end_date

dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
#NB: fixing the parsing of dates during csv read enables joining dates on matching values.
print "as read from SPY.csv file, dfSPY.columns.values.tolist()=", dfSPY.columns.values.tolist()

dfSPY = dfSPY.rename(columns = {'Adj Close':'SPY'})
print "after column renaming, dfSPY.columns.values.tolist()=", dfSPY.columns.values.tolist(), "dfSPY.shape=", dfSPY.shape

#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html

df1 = df1.join(dfSPY, how='inner')
print "after df1.join, df1.columns.values.tolist()=", df1.columns.values.tolist(), "df1.shape=", df1.shape

symbols = ['GOOG', 'IBM', 'GLD']
for symbol in symbols:
    print "reading csv file for ", symbol
    df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    print "csv file read"
    print "df_temp.columns.values.tolist()=", df_temp.columns.values.tolist()

    df_temp = df_temp.rename(columns = {'Adj Close':symbol})

    print "after col rename, df_temp.columns.values.tolist()=", df_temp.columns.values.tolist()
    df1 = df1.join(df_temp)
    #http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html
    #use how = 'inner'


#drop rows containing NaN
df1 = df1.dropna()
print "\nafter dropna df1.head(5)=\n", df1.head(5)
print "index values = df1.index.values=", df1.index.values
print "df1.columns.values.tolist()=", df1.columns.values.tolist()



