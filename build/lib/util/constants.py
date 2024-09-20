from pyspark.sql.types import StructType, StructField, StringType, IntegerType

class Constants:
    """
    Defines a series of constants variables that allow to
    reduce duplication
    """
    # base path
    _BASE_PATH = './data/{}'
    _TESTING_BASE_PATH = "./tests/mock/data/{}"
    
    _TEST_SCHEMA = StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True)
    ])
    
    _MOVIE_SCHEMA = StructType([
        StructField("MovieID", IntegerType(), True),
        StructField("Title", StringType(), True),
        StructField("Genres", StringType(), True)
    ])

    _USER_SCHEMA = StructType([
        StructField("UserID", IntegerType(), True),
        StructField("Gender", StringType(), True),
        StructField("Age", IntegerType(), True),
        StructField("Occupation", IntegerType(), True),
        StructField("Zip-Code", IntegerType(), True),
    ])
    
    _RATING_SCHEMA = StructType([
        StructField("UserID", IntegerType(), True),
        StructField("MovieID", IntegerType(), True),
        StructField("Rating", IntegerType(), True),
        StructField("Timestamp", IntegerType(), True)
    ])
