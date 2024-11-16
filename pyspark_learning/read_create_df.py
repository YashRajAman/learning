from pyspark.sql import SparkSession, Window
import pyspark.sql.functions as F


spark = SparkSession.builder.appName("Learning 1").master("local[*]").getOrCreate()

# Reading a file to create a dataframe csv/json. A range of types are supported.
print("Reading data from csv.")
df = spark.read.options(header=True).csv("/home/yash/MyWorkSpace/learning/retail_data.csv")
df.printSchema()
print(df.count(), len(df.columns), df.columns)

print("Reading data from json.")
df = spark.read.json("/home/yash/MyWorkSpace/learning/retail_data.json")
df.printSchema()
print(df.count(), len(df.columns), df.columns)


# df.write.json("/home/yash/MyWorkSpace/learning/retail_data.json")
# df.select("Customer ID", "Name", "Email").show(5)

# df.repartition(3)

# window_spec = Window.orderBy(F.monotonically_increasing_id())
# df_with_serial = df.withColumn("row_id", F.row_number().over(window_spec))
# df_with_serial.select("row_id", "Customer ID", "Name", "Email").show(5)

#===================

namelist = ["Yash", "Raj", "Aman"]
agelist  = [25,23,24]

print("\nZipping two lists.")
ageNamedf = spark.createDataFrame(data = zip(namelist, agelist), schema = ['name', 'agelist'])
ageNamedf.show()

print("Creating a dictionary and not passing schema")
ageNamedf = spark.createDataFrame(data = {"name":namelist, "age":agelist}.items())
ageNamedf.show()

print("Creating list of list.")
ageNamedf = spark.createDataFrame(data = [namelist, agelist], schema = ['name', 'agelist'])
ageNamedf.show()


"""
even though schema is provided in both lines.
zip multiple list
+----+-------+                                                                  
|name|agelist|
+----+-------+
|Yash|     25|
| Raj|     23|
|Aman|     24|
+----+-------+

Creating a dictionary and not passing schema
+----+-----------------+
|  _1|               _2|
+----+-----------------+
|name|[Yash, Raj, Aman]|
| age|     [25, 23, 24]|
+----+-----------------+

list of lists is different
all list must have same length
+----+-------+----+                                                             
|name|agelist|  _3|
+----+-------+----+
|Yash|    Raj|Aman|
|  25|     23|  24|
+----+-------+----+
"""

#===================