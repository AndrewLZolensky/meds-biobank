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

### Ontology Transforms

**Code Vocabulary**
- `vocab_id` / `concept_code`
- Original `concept_id`
- Categorizations (CCS, Phecodes)

**Measurement Representation**
- Decile-binned with zero-handling
