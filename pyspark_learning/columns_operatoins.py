from pyspark.sql import SparkSession, Window
import pyspark.sql.functions as F
import pyspark.sql.types as T

spark = SparkSession.builder.appName("Column Operations").master("local[*]").getOrCreate()

df    = spark.read.options(header=True).csv("/home/yash/MyWorkSpace/learning/retail_data.csv")

df.show(5)
size = df.count()
print("Total count of rows: ", size)

print("============SELECTING ONE OR MULTIPLE COLUMNS===============")
columns = df.columns

df.select(columns[0]).show(5)

df.select(columns[0], columns[1]).show(5)

df.select(columns[0:4]).show(5)

print("============Addition of Columns to the dataframe===============")

df = df.withColumn("A_Constant", F.lit(101))

columns = df.columns

print("New columns >> ", columns )

df.select(columns[-1:-3:-1]).show(5)

df = df.drop('A_Constant')

print("Columns after droping new columns > ", df.columns)

# Using a list for column values > It is a bit inconvenient

column_values = ["Yash" for _ in range(size)]
listdf        = spark.createDataFrame(data=[(x,) for x in column_values], schema=["A_Constant"])

# Adding a row number for a consistent row mapping.

listdf        = listdf.withColumn("row_id", F.row_number().over(Window.orderBy(F.monotonically_increasing_id())))
df            = df.withColumn("row_id", F.row_number().over(Window.orderBy(F.monotonically_increasing_id())))

df            = df.join(listdf, listdf.row_id == df.row_id).drop("row_id")

columns = df.columns

df.select(columns[-1:-3:-1]).show(5)