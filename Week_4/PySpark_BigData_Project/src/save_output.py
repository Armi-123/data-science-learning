def save_results(df):
    output_path = "data/output_city_stats"

    df.write.mode("overwrite").parquet(output_path)

    print(f"\n📁 Output saved safely to: {output_path}")
