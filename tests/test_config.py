import pytest
from vision_pipeline.config.loader import load_config

@pytest.fixture(scope="module")
def loaded_config():
    return load_config()

def test_loaded_config_is_dict(loaded_config):
    assert isinstance(loaded_config, dict)

@pytest.mark.parametrize(
    "section, expected_values, expected_types",
    [
        ("model", {"weights": "yolo11m.pt"}, {"weights": str}),
        (
            "inference",
            {"confidence": 0.5, "device": "cpu"},
            {"confidence": (int, float), "device": str},
        ),
        (
            "output",
            {"root": "outputs", "name": "predict", "save": True},
            {"root": str, "name": str, "save": bool},
        ),
        ("logging", {"level": "INFO"}, {"level": str}),
    ],
)
def test_config_sections(loaded_config, section, expected_values, expected_types):
    assert section in loaded_config
    assert loaded_config[section] is not None
    assert isinstance(loaded_config[section], dict)

    for key, expected_type in expected_types.items():
        assert key in loaded_config[section]
        assert isinstance(loaded_config[section][key], expected_type)

    for key, expected_value in expected_values.items():
        assert loaded_config[section][key] == expected_value