from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

class Utils:
    
    spark = SparkSession.builder.appName("NIQ_GFK").getOrCreate()
    
    @staticmethod
    def read_data(file_path: str,schema) -> DataFrame:
        """This function returns csv file which is being read from file_path

        Args:
            file_path (str): this contains the system file path where we kept the data
            schema (_type_): this has constant schema defined as per needs

        Raises:
            ValueError: When schema is not provided

        Returns:
            DataFrame: read dataframe
        """
        if schema=="" or schema is None:
            raise ValueError("Shema not provided")
        
        if file_path=="" or file_path is None:
            raise ValueError("File Path not provided")
        
        return Utils.spark.read.csv(file_path, header=True, schema=schema, sep="::")
        