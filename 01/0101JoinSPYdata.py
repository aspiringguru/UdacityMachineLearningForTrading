"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    #print df.head(4)
    df[['Close', 'Adj Close']].plot()
    # TODO: Your code here
    #add titles, legends, labels
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt..title("some title")
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
