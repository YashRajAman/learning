from pyspark.sql import SparkSession
from pyspark.sql.functions import array, col
from pyspark.ml.feature import HashingTF, NGram
from pyspark.ml import Pipeline
from pyspark.ml.feature import MinHashLSH

# Initialize Spark session
spark = SparkSession.builder \
    .appName("MySparkApp") \
    .master("local[*]") \
    .config("spark.local.dir", "/home/yash/MyWorkSpace/tmp") \
    .getOrCreate()

# Read data
df = spark.read.csv("/home/yash/MyWorkSpace/learning/retail_data.csv", header=True)

# Prepare the data
df = df.withColumn("first_names_array", array(df["Name"]))

# Define the pipeline stages
ngram = NGram(n=1, inputCol="first_names_array", outputCol="ngrams")
hashingTF = HashingTF(inputCol="ngrams", outputCol="features", numFeatures=100)
minhash = MinHashLSH(inputCol="features", outputCol="hashes", numHashTables=3)
pipeline = Pipeline(stages=[ngram, hashingTF, minhash])

# Fit the model
model = pipeline.fit(df)

# Transform the data
hashed_df = model.transform(df)

# Show features
hashed_df.select("features").show(truncate=False)

# Create a self-join for similarity comparison
similarity_df = model.stages[-1].approxSimilarityJoin(hashed_df, hashed_df, 0.6, "distance")

# Filter out self-comparisons by ensuring datasetA.id != datasetB.id (assuming there's an id column)
similarity_df_filtered = similarity_df.filter(col("datasetA.Name") != col("datasetB.Name"))

# Show results with similarity scores
similarity_df_filtered.select("datasetA.first_names_array", "datasetB.first_names_array", "distance").show(500, truncate=False)