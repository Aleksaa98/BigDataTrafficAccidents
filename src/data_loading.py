from spark_session import create_spark_session

def load_data_from_mongo():
    spark = create_spark_session()
    df = spark.read.format("mongodb") \
        .option("database", "TrafficAccidentsDB") \
        .option("collection", "Accidents") \
        .load()
    return df


if __name__ == "__main__":
    load_data_from_mongo()
