import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt


def main():
    print("Starting script")
    print("Loading jsons")

    print(sys.argv[1])
    df = pd.read_json(sys.argv[1])
    df = df.drop(columns=["header","title","titleUrl", "description", "products", "details", "activityControls", "subtitles"])


    
    df['hours'] = pd.to_datetime(df['time']).dt.hour #strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    print(df.groupby(["hours"]).count())
    print(df["hours"].count())
    sns.lineplot(df.groupby(["hours"]).count(), legend=None)

    plt.show()

    print("goodbye!")
    
if __name__ == '__main__':
    main()