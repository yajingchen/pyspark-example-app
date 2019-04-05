from pyspark.sql import SparkSession

from dataframe_utils.transforms import count_per_skill

if __name__ == '__main__':
    spark = SparkSession.builder.appName("pyspark-example-app").getOrCreate()

    input_df = spark.read.json("data")

    skills_count_df = count_per_skill(input_df)

    skills_count_df.coalesce(1).write.csv("output_data")
