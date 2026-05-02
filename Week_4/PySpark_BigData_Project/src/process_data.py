from pyspark.sql.functions import avg, max, min

def process_data(df):

    print("\n🔍 Filtering salary > 50,000...")
    high_salary = df.filter(df.salary > 50000)

    print("\n📊 Grouping by city...")
    city_stats = high_salary.groupBy("city_id").count()

    print("\n📈 Calculating salary statistics...")
    stats = df.agg(
        avg("salary").alias("avg_salary"),
        max("salary").alias("max_salary"),
        min("salary").alias("min_salary")
    )

    stats.show()
    city_stats.show()

    return city_stats
