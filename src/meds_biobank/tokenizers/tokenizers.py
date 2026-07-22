CUSTOM_CONCEPTS = {
    "IsHospitalAdmission": 700000001,
    "IsInpatientAdmission": 700000002,
    "IsObservation": 700000003,
    "IsEdVisit": 700000004,
    "IsOutpatientFaceToFaceVisit": 700000005,
    "IsVideoVisit": 700000007,
}

class Tokenizer():
    def __init__(self, custom_concepts=CUSTOM_CONCEPTS):
        self.custom_concepts = custom_concepts # concept_name, concept_id/code
        self.symbol_to_token = None
        self.token_to_symbol = None
        self.token_to_name = None
        self.token_to_description = None
        self.token_to_classifications = None

    def build_vocab(concepts, ccs=False, phecodes=False, med_ingred=False):
        """
        Args:
            concepts (pyspark.sql.DataFrame):
                Desc: OMOP concepts table
                Schema: |concept_id|vocabulary_id|concept_code|...
            ccs (bool):
                Desc: use ccs to build token_to_classifications
            phecodes (bool):
                Desc: use phecodes to build token_to_classifications
            med_ingred (bool):
                Desc: use med ingredients to build token_to_classifications
        
        Creates:
            symbol_to_token (Dict<int/String, int>):
                Desc: maps concept_id/code, decile bins, special tags/annotations, and custom concept ids to tokens
            token_to_symbol (Dict<int, int/String>):
                Desc: maps tokens to concept_id/code, decile bins, special tags/annotations, and custom concept ids
            token_to_name (Dict<int, String>):
                Desc: maps concept_id/code, decile bins, special tags/annotations, and custom concept ids to names
            token_to_description (Dict<int, String>):
                Desc: maps concept_id/code, decile bins, special tags/annotations, and custom concept ids to descriptions
            token_to_classifications (Dict<int, String>):
                Desc: maps concept_id/code, decile bins, special tags/annotations, and custom concept ids to classifications list
        """
        # TODO: create maps
        pass
    
    def tokenize(events, rollout=False):
        """
        Args:
            events (List<Dict>):
                Desc: Records for a single patient, ordered by time, desc
                Dict Schema: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|
                Notes:
                    • code = concept_id
                    • text_value for labs_/vitals_ event types will be bins and be tokenized separately after the concept itself
                    • raw measurement events will have value skipped
                    • add BOS
            rollout (bool):
                Desc: if true, apply rollout tokenization using classifications preceding specific code token(s)
        Returns:
            tokens (List<int>), times (List<timestamp>)
        """
        pass
    
    def insert_time_tokens(tokens, times):
        pass
    
    def decode(tokens):
        # decode into events: |patient_id|code|time|end|numeric_value|text_value|unit|event_type|visit_id|
        pass
    
    def visualize(tokens):
        pass