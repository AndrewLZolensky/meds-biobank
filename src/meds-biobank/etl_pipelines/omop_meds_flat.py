import pyspark.sql.functions as sf

def omop_table_to_meds_events(omop_table, table_name):
    """
    Convert an OMOP table into MEDS-formatted events.

    Args:
        omop_table (pyspark.sql.DataFrame): OMOP events table with columns
            "person_id", "concept_id", "{table_name}_start_date", ...
        table_name (str): OMOP table name (e.g. "visit_occurrence", "drug_exposure")

    Returns:
        pyspark.sql.DataFrame: Events in MEDS format
    """
    pass

def gather_meds_events(meds_tables):
    """
    Compile separate events tables into a single table
    """
    pass

def prune_meds_events(meds_events):
    """
    Prune/deduplicate patient event streams
    """
    pass

def convert_to_patient_streams(meds_events):
    """
    Order by patient and time
    """
    pass