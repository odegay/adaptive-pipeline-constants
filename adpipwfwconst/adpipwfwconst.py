from enum import Enum

class MSG_TYPE(Enum):
    ADAPTIVE_PIPELINE_START = 0
    START_MODEL_CONFIGURATION = 1
    REQUEST_LLM_NEW_MODEL_CONFIGURATION = 2
    NEW_MODEL_CONFIGURATION_SUCCESS = 3
    NEW_MODEL_CONFIGURATION_FAILURE = 4
    GENERATE_NEW_MODEL = 5
    NEW_MODEL_GENERATION_SUCCESS = 6
    NEW_MODEL_GENERATION_FAILURE = 7
    PREPARE_FEATURES = 8
    FEATURES_PREPARATION_SUCCESS = 9
    FEATURES_PREPARATION_FAILURE = 10
    START_PREDICTION = 11
    PREDICTION_SUCCESS = 12
    PREDICTION_FAILURE = 13
    MODEL_FITS_KPIS = 14
    MODEL_MISSING_KPIS = 15
    ADAPTIVE_PIPELINE_END = 16
    ADAPTIVE_PIPELINE_ERROR = 17

class PIPELINE_TOPICS(Enum):
    WORKFLOW_TOPIC = "adaptive-pipeline-workflow-topic"
    CONFIG_TOPIC = "adaptive-pipeline-config-topic"
    FEATURES_TOPIC = "adaptive-pipeline-features-topic"
    MODEL_TOPIC = "adaptive-pipeline-model-topic"
    PREDICTION_TOPIC = "adaptive-pipeline-prediction-topic"    
    ERROR_TOPIC = "adaptive-pipeline-error-topic"