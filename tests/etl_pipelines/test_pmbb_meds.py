from meds_biobank.etl_pipelines.pmbb_meds import extract_events

def test_extract_events_person(spark, person):
    result = extract_events(person, "person")
    assert set(result.columns) == {"patient_id", "time", "code", "event_type", "value", "end", "visit_id", "unit", "measurement_id"}
    result.collect()  # forces Spark to actually run the transformation