import matplotlib.pyplot as plt
import pandas as pd


def load_data():
    df = pd.read_csv("stats.csv", index_col="timestamp", names=["timestamp", "downloads", "stars"], parse_dates=True)
    return df


if __name__ == "__main__":
    df = load_data()
    df = df.resample('1D').mean()
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2, sharex=ax1)

    df.plot(ax=ax1)
    ax1.set_title("Cumulative")
    ax1.set_ylim(0)

    df_d = df.diff()
    df_d = df_d[df_d > 0]    # Filter out the crazy outlier
    df_d.plot(ax=ax2)
    ax2.set_title("Per day")
    ax2.set_ylim(0)

    plt.show()
    print(df)
