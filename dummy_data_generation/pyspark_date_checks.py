from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, to_timestamp

# initialize Spark
spark = SparkSession.builder.appName("Date Conversion").getOrCreate()
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")
# create a sample dataframe
data = [("2023-02-20 12:34:55",), ("2023-06-15 14:30:00",), ("2023-24-20 22:34:55",)]
df = spark.createDataFrame(data, ["date_string"])

# use to_date and to_timestamp functions
df = df.select(
    "date_string",
    to_date(col("date_string"), "yyyy-MM-dd HH:mm:ss").alias("to_date"),
    to_timestamp(col("date_string"), "yyyy-mm-dd hh:mm:ss").alias("to_timestamp")
)

# print the output
df.show(truncate=False)