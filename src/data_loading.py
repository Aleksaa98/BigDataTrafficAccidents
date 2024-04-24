from spark_session import create_spark_session

spark = create_spark_session()

def load_data_from_mongo(spark):
    df = spark.read.format("mongodb").load()
    print("============================================================================")

