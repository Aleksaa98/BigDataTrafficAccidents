from pyspark.sql import SparkSession

# spark = SparkSession.builder\
#     .appName("TrafficAccidentsAnalysis") \
#     .config("spark.mongodb.input.uri", "mongodb://127.0.0.1:27017/TrafficAccidentsDB.Accidents?readPreference"
#                                        "=primaryPreferred") \
#     .config("spark.mongodb.output.uri", "mongodb://127.0.0.1:27017/TrafficAccidentsDB.Accidents") \
#     .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.2")\
#     .getOrCreate()


def create_spark_session():
    spark = SparkSession.builder \
        .appName("TrafficAccidentsAnalysis") \
        .config("spark.mongodb.input.uri", "mongodb://localhost:27017/TrafficAccidentsDB.Accidents?readPreference"
                                           "=primaryPreferred") \
        .config("spark.mongodb.output.uri", "mongodb://localhost:27017/TrafficAccidentsDB.Accidents") \
        .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.2") \
        .getOrCreate()

    print("=============================================")
    return spark



