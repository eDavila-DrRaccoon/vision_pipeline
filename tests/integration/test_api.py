from pathlib import Path

from fastapi.testclient import TestClient

from vision_pipeline.api.app import app

client = TestClient(app)

TEST_IMAGE = Path("examples/images/dog.jpg")
INVALID_FILE = Path("tests/resources/dummy.txt")


# ------------------------------------------------------------------
# Path endpoint
# ------------------------------------------------------------------

class TestPathInference:
    
    def test_path_inference_valid_image(self):
        response = client.post(
            "/inference/path",
            json={
                "image": str(TEST_IMAGE)
            },
        )

        assert response.status_code == 200

        body = response.json()

        assert body["status"] == "success"
        assert "message" in body
        assert "data" in body
        assert "output_directory" in body["data"]


    def test_path_inference_missing_image(self):
        response = client.post(
            "/inference/path",
            json={
                "image": "examples/images/does_not_exist.jpg"
            },
        )

        assert response.status_code == 404


    def test_path_inference_unsupported_extension(self):
        response = client.post(
            "/inference/path",
            json={
                "image": str(INVALID_FILE)
            },
        )

        assert response.status_code == 400


# ------------------------------------------------------------------
# Upload endpoint
# ------------------------------------------------------------------

class TestUploadInference:

    def test_upload_valid_image(self):
        with TEST_IMAGE.open("rb") as image:

            response = client.post(
                "/inference/upload",
                files={
                    "image": (
                        TEST_IMAGE.name,
                        image,
                        "image/jpeg",
                    )
                },
            )

        assert response.status_code == 200

        body = response.json()

        assert body["status"] == "success"
        assert "message" in body
        assert "data" in body
        assert "output_directory" in body["data"]


    def test_upload_invalid_mime_type(self):
        with INVALID_FILE.open("rb") as file:

            response = client.post(
                "/inference/upload",
                files={
                    "image": (
                        "dummy.jpg",
                        file,
                        "text/plain",
                    )
                },
            )

        assert response.status_code == 400


    def test_upload_unsupported_extension(self):
        with INVALID_FILE.open("rb") as file:

            response = client.post(
                "/inference/upload",
                files={
                    "image": (
                        "dummy.gif",
                        file,
                        "image/gif",
                    )
                },
            )

        assert response.status_code == 400