from sklearn.ensemble import IsolationForest
from visualization import visualize_anomalies
import matplotlib.pyplot as plt


# Function to fit Isolation Forest and return a DataFrame with anomalies
def fit_isolation_forest(pandas_df):
    features = ['Latitude', 'Longitude', 'Collision Type_numeric', 'Light_numeric', 'VEH#', 'Weather_numeric','DATETIME_COMBINED']
    if any(col not in pandas_df.columns for col in features):
        raise ValueError("Missing one or more expected features for Isolation Forest")

    isolation_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)

    isolation_forest.fit(pandas_df[features])

    pandas_df['anomaly_score'] = isolation_forest.decision_function(pandas_df[features])
    pandas_df['anomaly'] = isolation_forest.predict(pandas_df[features])

    anomalies = pandas_df[pandas_df['anomaly'] == -1]
    plt.figure(figsize=(10, 6))
    plt.hist(pandas_df['anomaly_score'], bins=30, alpha=0.7, label='Normal')
    plt.hist(anomalies['anomaly_score'], bins=30, alpha=0.7, label='Anomaly')
    plt.xlabel('Anomaly Score')
    plt.ylabel('Count')
    plt.title('Anomaly Score Distribution')
    plt.legend()
    plt.show()
    print(pandas_df.head(5))

    return pandas_df


def analyze_data(df, decode_mapping):
    df_with_anomalies = fit_isolation_forest(df)
    print("Columns in DataFrame:", df_with_anomalies.columns)
    visualize_anomalies(df_with_anomalies, decode_mapping)


if __name__ == "__main__":
    from data_loading import load_data_from_mongo
    from processing import clean_and_prepare_data

    df = load_data_from_mongo()
    cleaned_pandas_df, decode_mapping = clean_and_prepare_data(df)

    analyze_data(cleaned_pandas_df, decode_mapping)
