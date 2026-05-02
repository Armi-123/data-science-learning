from pyspark.sql import SparkSession

def create_spark():
    spark = SparkSession.builder \
        .appName("LocalBigDataSafe") \
        .master("local[*]") \
        .config("spark.driver.memory", "1g") \
        .config("spark.sql.shuffle.partitions", "4") \
        .getOrCreate()
    return spark
