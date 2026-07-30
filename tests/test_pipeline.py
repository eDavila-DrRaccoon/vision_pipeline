import pytest
from vision_pipeline.pipelines.inference import run_inference

def test_run_inference_missing_image():
    with pytest.raises(FileNotFoundError):
        run_inference("this/image/does/not/exist.jpg")
