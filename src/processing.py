from pyspark.sql.functions import col
from data_loading import load_data_from_mongo
from pyspark.sql.types import IntegerType, FloatType
from datetime import datetime, timedelta
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)


def convert_days_to_human_date(days_since_epoch):
    epoch_start = datetime(1970, 1, 1)
    human_date = epoch_start + timedelta(days=days_since_epoch)
    return human_date.strftime('%Y-%m-%d')  # Format date as a string


def convert_time_to_numeric(time_str):
    try:
        dt = datetime.strptime(time_str, '%I:%M %p')
    except ValueError:
        try:
            dt = datetime.strptime(time_str, '%H%M')
        except ValueError:
            return None
    return dt.hour * 60 + dt.minute


def convert_date_to_numeric(date_str):
    return (datetime.strptime(date_str, '%m/%d/%Y') - datetime(1970, 1, 1)).days


def convert_to_numeric(df, columns, fill_value=0):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(fill_value)
    return df

# Data cleaning and preparation for Isolation Forest


def clean_and_prepare_data(df):
    sorted_df = df.select('Collision Type', 'DATE', 'DEAD', 'INJ', 'Latitude', 'Light', 'Locality', 'Longitude', 'Primary Factor',
                          'Road Char', 'Road Class', 'Rumble Strips', 'TIME', 'Surf Con', 'Surface', 'VEH#', 'Weather')

    sorted_df = sorted_df.fillna(-1)

    sorted_df = sorted_df.withColumn("VEH#", sorted_df["VEH#"].cast(IntegerType()))
    sorted_df = sorted_df.withColumn("INJ", sorted_df["INJ"].cast(IntegerType()))
    sorted_df = sorted_df.withColumn("DEAD", sorted_df["DEAD"].cast(IntegerType()))
    sorted_df = sorted_df.withColumn("Latitude", sorted_df["Latitude"].cast(FloatType()))
    cleaned_df = sorted_df.withColumn("Longitude", sorted_df["Longitude"].cast(FloatType()))
    cleaned_df = cleaned_df.filter((col("Latitude") != 0) & (col("Longitude") != 0))
    print(cleaned_df.show(20))
    pandas_df = cleaned_df.toPandas()

    decoded_mappings = {}
    for column in ['Collision Type', 'Light', 'Locality', 'Primary Factor', 'Weather']:
        cat = pd.Categorical(pandas_df[column])
        pandas_df[column + '_numeric'] = pd.Categorical(pandas_df[column]).codes + 1
        decoded_mappings[column] = {i + 1: label for i, label in enumerate(cat.categories)}

    print("====================")

    pandas_df['DATE_NUMERIC'] = pandas_df['DATE'].apply(
        lambda x: (datetime.strptime(x, '%m/%d/%Y') - datetime(1970, 1, 1)).days
    )
    pandas_df['TIME_NUMERIC'] = pandas_df['TIME'].apply(convert_time_to_numeric)
    pandas_df = pandas_df.dropna(subset=['TIME_NUMERIC'])
    pandas_df['DATETIME_COMBINED'] = pandas_df['DATE_NUMERIC'] + pandas_df['TIME_NUMERIC'] / (24 * 60)

    print(pandas_df.head(10))

    return pandas_df,decoded_mappings


if __name__ == "__main__":
    df = load_data_from_mongo()
    cleaned_pandas_df = clean_and_prepare_data(df)