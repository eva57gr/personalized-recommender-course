from enum import Enum
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomerDatasetSize(Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    HOPSWORKS_API_KEY: SecretStr | None = None

    RECSYS_DIR: Path = Path(__file__).parent

    # Feature engineering
    CUSTOMER_DATA_SIZE: CustomerDatasetSize = CustomerDatasetSize.SMALL
    FEATURES_EMBEDDING_MODEL_ID: str = "all-MiniLM-L6-v2"

    # Training
    TWO_TOWER_MODEL_EMBEDDING_SIZE: int = 16
    TWO_TOWER_MODEL_BATCH_SIZE: int = 2048
    TWO_TOWER_NUM_EPOCHS: int = 10
    TWO_TOWER_WEIGHT_DECAY: float = 0.001
    TWO_TOWER_LEARNING_RATE: float = 0.01
    TWO_TOWER_DATASET_VALIDATON_SPLIT_SIZE: float = 0.1
    TWO_TOWER_DATASET_TEST_SPLIT_SIZE: float = 0.1

    TWO_TOWER_DATASET_VALIDATON_SPLIT_SIZE: float = 0.1


settings = Settings()
