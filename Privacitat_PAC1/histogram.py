import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt


def main():
    print(sys.argv[1])
    df = pd.read_json(sys.argv[1])
    df = df.drop(columns=["header","title","titleUrl", 
    "description", "products", "details", "activityControls", "subtitles"])

    df['hour'] = pd.to_datetime(df['time']).dt.hour 
    sns.lineplot(df.groupby(["hour"]).count(), legend=None)
    plt.ylabel("views")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()