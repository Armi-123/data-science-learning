from src.spark_session import create_spark
from src.generate_data import create_big_data
from src.process_data import process_data
from src.save_output import save_results

def run():
    print("\n🔧 Starting Spark Session...")
    spark = create_spark()

    print("\n📦 Generating Safe Big Dataset...")
    df = create_big_data(spark)

    print("\n⚙️ Processing Data...")
    result_df = process_data(df)

    print("\n💾 Saving Output...")
    save_results(result_df)

    print("\n✅ Big Data Pipeline Completed Successfully!")

if __name__ == "__main__":
    run()
