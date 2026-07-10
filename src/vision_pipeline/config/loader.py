from pathlib import Path

import yaml

def load_config(config_path: Path | None = None) -> dict:
    """
    Load the project configuration from a YAML file.
    """

    if config_path is None:
        config_path = Path("configs/default.yaml")

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config