from pyspark.sql import SparkSession
from util.utils import Utils 
from util.constants import Constants
import pytest

@pytest.fixture(scope="module")
def spark_session():
    """Create a Spark session."""
    spark = SparkSession.builder \
        .appName("NIQ_GFK_Test") \
        .getOrCreate()
    yield spark
    spark.stop()

def test_read_data(spark_session):
    # Use the read_data method to read the data
    df = Utils.read_data(Constants._TESTING_BASE_PATH.format('test_data.csv'),Constants._TEST_SCHEMA)

    # Verify the DataFrame schema
    assert df.schema == Constants._TEST_SCHEMA
    
    # Verify the data
    expected_data = [(1, "John"), (2, "Doe"), (3, "Alice")]
    actual_data = df.collect()
    assert [(row.id, row.name) for row in actual_data] == expected_data
    
def test_read_data_without_schema(spark_session):
    # Assert that calling read_data without schema raises a ValueError
    with pytest.raises(ValueError):
        Utils.read_data(Constants._TESTING_BASE_PATH.format('test_data.csv'), schema=None)
        
def test_read_data_without_file_path(spark_session):
    # Assert that calling read_data without path raises a ValueError
    with pytest.raises(ValueError):
        Utils.read_data(None, schema=Constants._TEST_SCHEMA)