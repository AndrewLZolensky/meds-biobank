# meds-biobank
This is an UNOFFICIAL lightweight python re-implementation of several parts of the MEDS software ecosystem. It is designed to operate on in-memory tables loaded via pyspark, rather than directly on disk. It is intended for users of small to medium-scale biobanks, which are often queried via cloud services from Interactive Python Notebooks.

At this time the package is primarily developed for use with Penn Medicine Biobank.

# Features

## ETL
### 👴 omop meds-etl 0.1.3
#### path
/meds-biobank/src/meds-biobank/etl_pipelines/omop_meds_nwsted.py
#### description
re-implementation of src/meds_etl/omop.py from the meds_etl package version 0.1.3 which outputs from OMOP v5.4/5.3 to MEDS v0.1.3 (nested format, use this with CLMBR-T-base/FEMR v0.2.3)
#### workflow
1. Extract all events
2. Prune/deduplicate patient event streams
3. Convert event streams into nested patient representations
#### differences from source
Prune (delta_encode, remove_nones) before finalizing the meds mapping.
#### Supported Tables
- person
- visit_occurrence
- procedure_occurrence
- condition_occurrence
- drug_exposure
- observation
- measurements
- death
### options
- Pre-ETL of measurements yielding value and unit conversion and separation into labs and vitals (sub-options: where possible vs. drop messy)

### 👶 omop meds-etl 0.3.11
#### path
/meds-biobank/src/meds-biobank/etl_pipelines/omop_nested_flat.py
#### description
A re-implementation of src/meds_etl/omop.py from the meds_etl package version 0.3.11 which outputs from OMOP v5.4/5.3 to MEDS v0.3.3 (flat format, handles visit discharge).
#### workflow
1. Extract all events
2. Prune/deduplicate patient event streams
3. Order event streams by patient, time
#### differences from source
Prune (delta_encode, remove_nones) within the etl rather than as part of the tokenizer (FEMR 0.2.3, transforms sub-module).
#### Supported Tables
- person
- visit_occurrence
- procedure_occurrence
- condition_occurrence
- drug_exposure
- observation
- measurements
- death
### options
- Pre-ETL of measurements yielding value and unit conversion and separation into labs and vitals (sub-options: where possible vs. drop messy)

## Ontology Transforms
### Code Vocabulary
- vocab_id/concept_code
- original concept_id
- Categorizations (CCS, Phecodes)
### Measurement Representation
- decile-binned with zero-handling