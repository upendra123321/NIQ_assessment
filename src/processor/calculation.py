from util.constants import Constants
from util.utils import Utils
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType

# Create all 3 dfs here 
movies_df = Utils.read_data(Constants._BASE_PATH.format('movies.dat'),Constants._MOVIE_SCHEMA)
users_df = Utils.read_data(Constants._BASE_PATH.format('users.dat'),Constants._USER_SCHEMA)
ratings_df = Utils.read_data(Constants._BASE_PATH.format('ratings.dat'),Constants._RATING_SCHEMA)

# Extract year from the title and explode the genres
movies_df = movies_df.withColumn("Year", F.regexp_extract(F.col("Title"), r'\((\d{4})\)', 1).cast(IntegerType()))\
                     .withColumn("Genre", F.explode(F.split(F.col("Genres"), r'\|')))

# Filter users by non-null zip code and age range 18-59
users_df = users_df.filter(F.col("Zip-Code").isNotNull()).select("UserID", "Age")
ratings_users_bw_18_50 = ratings_df.join(users_df, on = "UserID").filter(F.col("Age").between(18, 49))

# Join ratings with movies, filter movies released after 1989, group by genre and year, and calculate average rating
average_ratings_df = (ratings_users_bw_18_50
                      .join(movies_df, on="MovieID")
                      .filter(F.col("Year") > 1989)
                      .groupBy("Genre", "Year")
                      .agg(F.avg("Rating").alias("avg_rating"))
                      .orderBy("Year"))

average_ratings_df.show()

Utils.spark.stop()