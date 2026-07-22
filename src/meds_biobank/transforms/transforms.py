def etl_measurements(events):
    """
    Args:
        events (pyspark.sql.DataFrame):
            Desc: MEDS events table
            Schema: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|

    Returns:
        events (pyspark.sql.DataFrame):
            Desc:
            Schema: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|
    """
    # TODO: maps labs and vitals through cleanup and update event types accordingly
    pass

def bin_measurements(events):
    """
    Args:
        events (pyspark.sql.DataFrame):
            Desc: MEDS events table
            Schema: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|

    Returns:
        events (pyspark.sql.DataFrame):
            Desc:
            Schema: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|
        mappings:
            Desc:
            • map from lab/vitals event_type ("labs_/vitals_<type>") to decile bin values
            • map from codes/concept_ids to labs/vitals category
    """
    # TODO: bin measurements into deciles (w/ separate 0 case)
    pass

def rollup_concepts(events, concept_ancestor):
    """
    Args:
        events (pyspark.sql.DataFrame):
            Desc: MEDS events table
            Schema: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|
        concept_ancestor (pyspark.sql.DataFrame):
            Desc:
            Schema:

    Returns:
        events (pyspark.sql.DataFrame):
            Desc:
            Schema: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|
    """
    # TODO: option to rollup infrequent concepts into frequent ancestors, and optionally drop non-mapped
    pass