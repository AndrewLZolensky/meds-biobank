# meds-biobank

> Unofficial, lightweight Python re-implementation of parts of the **MEDS** software ecosystem, built to operate on in-memory tables loaded via PySpark rather than directly on disk. Designed for small-to-medium biobanks queried through cloud services in interactive Python notebooks.

**Primary target:** Penn Medicine Biobank

---

## Table of Contents

- [Features](#features)
  - [ETL](#etl)
    - [OMOP MEDS-ETL 0.1.3 (Nested)](#-omop-meds-etl-013)
    - [OMOP MEDS-ETL 0.3.11 (Flat)](#-omop-meds-etl-0311)
  - [Ontology Transforms](#ontology-transforms)

---

## Features

### ETL

#### OMOP MEDS-ETL 0.1.3

| | |
|---|---|
| **Path** | `/meds-biobank/src/meds-biobank/etl_pipelines/omop_meds_nwsted.py` |
| **Description** | Re-implementation of `src/meds_etl/omop.py` from `meds_etl` v0.1.3. Converts OMOP v5.4/5.3 → MEDS v0.1.3 (nested format). Use with CLMBR-T-base / FEMR v0.2.3. |

**Workflow**
1. Extract all events
2. Prune / deduplicate patient event streams
3. Convert event streams into nested patient representations

**Differences from source**
Pruning (`delta_encode`, `remove_nones`) happens *before* finalizing the MEDS mapping.

**Supported Tables**
`person` · `visit_occurrence` · `procedure_occurrence` · `condition_occurrence` · `drug_exposure` · `observation` · `measurements` · `death`

**Options**
- Pre-ETL of measurements: value/unit conversion + separation into labs and vitals
  - Sub-options: *where possible* vs. *drop messy*

---

#### OMOP MEDS-ETL 0.3.11

| | |
|---|---|
| **Path** | `/meds-biobank/src/meds-biobank/etl_pipelines/omop_nested_flat.py` |
| **Description** | Re-implementation of `src/meds_etl/omop.py` from `meds_etl` v0.3.11. Converts OMOP v5.4/5.3 → MEDS v0.3.3 (flat format, handles visit discharge). |

**Workflow**
1. Extract all events
2. Prune / deduplicate patient event streams
3. Order event streams by patient, time

**Differences from source**
Pruning (`delta_encode`, `remove_nones`) happens *within the ETL*, rather than as part of the tokenizer (FEMR 0.2.3 `transforms` sub-module).

**Supported Tables**
`person` · `visit_occurrence` · `procedure_occurrence` · `condition_occurrence` · `drug_exposure` · `observation` · `measurements` · `death`

**Options**
- Pre-ETL of measurements: value/unit conversion + separation into labs and vitals
  - Sub-options: *where possible* vs. *drop messy*

---

#### PMBB OMOP MEDS-ETL

**Specification**
Outputs in the format:
```bash
|patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|
```
Special Notes:
1. code is an OMOP concept id. Unless explicitly specified via boolean flag, it is the standardized OMOP concept id.
2. time is the time of event, end is optional
3. numeric_value and unit contain ETL'd values for a large subset of measurements pre-extracted into labs_ and vitals_ tables with value_converted and unit_converted columns
4. event_type contains the source OMOP domain for the table (e.g. measurement, procedure, etc.) EXCEPT for labs and vitals which are formatted as "labs_"/"vitals_" + name e.g. "labs_albumin"

Flags:
1. If the OMOP extract only yields measurements, there is (will be) separate ETL logic in /transforms to transform the data into the right form.

---

### Tokenizers

---

### Transforms

**etl_labs_vitals**
Expects events table in the format |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|. Performs labs/vitals ETL.

**etl_labs_vitals**
Expects events table in the format |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|. Post labs/vitals ETL. Extracts mapping from omop concept ids to labs_/vitals_ names