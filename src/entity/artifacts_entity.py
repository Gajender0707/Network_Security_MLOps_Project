import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifacts:
    training_data_path:Path
    testing_data_path:Path