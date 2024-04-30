import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def visualize_anomalies(df, decode_mapping):
    plt.figure(figsize=(14, 8))
    plt.subplots_adjust(left=0.2, bottom=0.15, right=0.8, top=0.9)
    df['Decoded_Collision_Type'] = df['Collision Type_numeric'].map(decode_mapping['Collision Type'])
    df['Decoded_Weather'] = df['Weather_numeric'].map(decode_mapping['Weather'])
    df['Human_Date'] = pd.to_datetime(df['DATETIME_COMBINED'], unit='D', origin='1970-01-01')
    sns.scatterplot(
        x='VEH#',
        y='Decoded_Collision_Type',
        hue='anomaly',
        data=df,
        palette={1: 'green', -1: 'red'},
        style='anomaly',
        markers={1: 'o', -1: 'X'},
        s=100
    )
    plt.title('Accidents Over Time with Anomalies')
    plt.xlabel('Number of Vehicles ')
    plt.ylabel('Collision Type')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='Longitude',
        y='Latitude',
        hue='anomaly',
        data=df,
        palette={1: 'green', -1: 'red'},
        style='anomaly',
        markers={1: 'o', -1: 'X'},
        s=100
    )
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Accidents by Geographic Location')
    plt.show()

    # plt.figure(figsize=(14, 8))
    # sns.scatterplot(
    #     x='Human_Date',
    #     y='Decoded_Collision_Type',
    #     hue='anomaly',
    #     data=df,
    #     palette={1: 'green', -1: 'red'},
    #     style='anomaly',
    #     markers={1: 'o', -1: 'X'},
    #     s=100
    # )
    # plt.title('Accidents by Year and Collision Type')
    # plt.xlabel('Year')
    # plt.ylabel('Collision Type')
    # plt.show()
