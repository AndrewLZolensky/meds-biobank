import pytest
from pyspark.sql import SparkSession
from pathlib import Path

@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder
        .master("local[2]")
        .appName("meds-biobank-tests")
        .config("spark.sql.shuffle.partitions", "2")
        .getOrCreate()
    )

@pytest.fixture(scope="session")
def data_dir():
    return Path(__file__).resolve().parent.parent / "data"

@pytest.fixture(scope="session")
def concept_ancestor(spark, data_dir):
    return spark.read.csv(str(data_dir / "concept_ancestor.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def concept(spark, data_dir):
    return spark.read.csv(str(data_dir / "concept.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def condition_occurrence(spark, data_dir):
    return spark.read.csv(str(data_dir / "condition_occurrence.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def death(spark, data_dir):
    return spark.read.csv(str(data_dir / "death.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def drug_exposure(spark, data_dir):
    return spark.read.csv(str(data_dir / "drug_exposure.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def measurement(spark, data_dir):
    return spark.read.csv(str(data_dir / "measurement.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def observation(spark, data_dir):
    return spark.read.csv(str(data_dir / "observation.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def person(spark, data_dir):
    return spark.read.csv(str(data_dir / "person.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def procedure_occurrence(spark, data_dir):
    return spark.read.csv(str(data_dir / "procedure_occurrence.csv"), header=True, inferSchema=True)

@pytest.fixture(scope="session")
def visit_occurrence(spark, data_dir):
    return spark.read.csv(str(data_dir / "visit_occurrence.csv"), header=True, inferSchema=True)