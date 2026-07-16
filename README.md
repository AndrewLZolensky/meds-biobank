# meds-biobank
This is an UNOFFICIAL lightweight python re-implementation of several parts of the MEDS software ecosystem. It is designed to operate on in-memory tables loaded via pyspark, rather than directly on disk. It is intended for users of small to medium-scale biobanks, which are often queried via cloud services from Interactive Python Notebooks.

# Features

## omop meds-etl 0.1.3
### description
re-implementation of src/meds_etl/omop.py from the meds_etl package version 0.1.3 which outputs from OMOP v5.4/5.3 to MEDS v0.1.3 (nested format, use this with CLMBR-T-base/FEMR v0.2.3)
### differences from source
Prune (delta_encode, remove_nones) before finalizing the meds mapping.

## omop meds-etl 0.3.11
### description
A re-implementation of src/meds_etl/omop.py from the meds_etl package version 0.3.11 which outputs from OMOP v5.4/5.3 to MEDS v0.3.3 (flat format, handles visit discharge).
### differences from source
Prune (delta_encode, remove_nones) within the etl rather than as part of the tokenizer (FEMR 0.2.3, transforms sub-module).

# ETL Workflow
1. Extract all events
2. Prune/deduplicate patient event streams
3. Order by patient id, time

# Supported Tables
- person
- visit_occurrence
- procedure_occurrence
- condition_occurrence
- drug_exposure
- observation
- measurements
- death

# Options
1. Vocabulary:
    a. vocab_id/concept_code (prioritize source concept)
    b. original concept_id
    c. Categorizations (CCS, Phecodes)
2. Measurements
    a. Native meds-etl 0.3.11
        value = coalesce(value_as_number, value_as_string, backup)
            backup = ...
            -> If: nonzero/nonull value_as_concept_id
                -> If: nonull/nonzero source concept id
                    -> value = SOURCE_CODE/source_value, otherwise
                -> Else:
                    -> value = OMOP_CONCEPT_ID/value_as_concept_id
            -> Else: null
    b. PMBB-ETL
        - retain only ETL'd measurements, dropping nulls
        - Optionally, bin the values to deciles w/ separate cat for 0's
    c. both
        - save as raw_value, etl_value