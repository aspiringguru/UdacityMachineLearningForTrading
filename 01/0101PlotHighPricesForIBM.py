"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    #print df.head(4)
    df['High'].plot()
    # TODO: Your code here
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
