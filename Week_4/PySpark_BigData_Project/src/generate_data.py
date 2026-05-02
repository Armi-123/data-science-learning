from pyspark.sql.functions import rand, round as spark_round

def create_big_data(spark):

    # Safe row count for ANY laptop
    row_count = 200000  

    df = spark.range(0, row_count) \
        .withColumn("age", (rand() * 60 + 20).cast("int")) \
        .withColumn("salary", spark_round(rand() * 90000 + 30000, 2)) \
        .withColumn("city_id", (rand() * 10).cast("int"))

    df.show(5)
    print(f"\n📊 Generated {row_count:,} rows safely.")

    return df
