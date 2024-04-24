from pyspark.sql.functions import col, when


def process_data(df):
    # Fill missing latitude and longitude with zero
    df = df.na.fill(0, subset=["latitude", "longitude"])

    # Example: Adding a new column to indicate night or day
    df = df.withColumn("is_night", when(col("Light") == "DARK", True).otherwise(False))

    return df