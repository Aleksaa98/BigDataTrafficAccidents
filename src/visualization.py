import matplotlib.pyplot as plt
import seaborn as sns


def visualize_data(pandas_df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=pandas_df, x="longitude", y="latitude", hue="Light")
    plt.title("Traffic Accidents by Location")
    plt.show()
