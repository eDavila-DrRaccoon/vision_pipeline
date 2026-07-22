<!-- 
Title and description included in `_config.yml`

# Vision Pipeline

Production-oriented Computer Vision inference framework featuring FastAPI, Docker, YOLO11, YAML configuration and modular architecture. --> 

Production-oriented Computer Vision Inference Framework.

Vision Pipeline is a modular FastAPI-based framework designed to simplify the development and deployment of computer vision inference services as maintainable software products. Rather than focusing on model development, it emphasizes software engineering through combining reproducible Docker environments, YAML-based configuration, REST APIs, structured logging, and a YOLO11 inference pipeline within a clean and extensible architecture, with planned support for multiple inference backends including PyTorch, ONNX Runtime, and TensorRT. 

The project demonstrates how modern AI inference systems can be engineered as **modular, reproducible, and production-ready software products**.

**🚧 Active Development**  
The project is part of the AI Engineering Portfolio and focuses on clean software architecture, modular inference backends and reproducible deployment ([Back to the Portfolio Hub](https://edavila-drraccoon.github.io/portfolio_site/)). 

## Technology Stack & Features
---

| Category | Technology / Feature |
|----------|----------------------|
| Architecture | Modular package architecture |
| Language | Python 3.13 |
| Packaging | `pyproject.toml` |
| Deployment | Docker + Docker Compose |
| REST API | FastAPI |
| API Documentation | OpenAPI / Swagger UI |
| Configuration | YAML |
| Response Format | Uniform JSON contract |
| Error Handling | Global exception handler |
| Logging | Python logging |
| CLI | Command-line interface |
| Deep Learning | PyTorch |
| Model | YOLO11 object detection |

## Quick Start
---

```bash
git clone https://github.com/eDavila-DrRaccoon/vision_pipeline.git
cd vision_pipeline
docker compose up --build
```

The service will be available at:
```text
http://localhost:8000/docs
```

FastAPI automatically exposes an interactive Swagger UI and the OpenAPI specification at this address.

On the first execution, the application will:

- build the Docker image
- start the FastAPI service
- download the YOLO11 model automatically (first request only)
- perform object detection after an inference request
- save the annotated image to the configured output directory (default: `outputs/predict/`)

## REST API
---

Once the service is running, open:
```
http://localhost:8000/docs
```

FastAPI automatically generates an OpenAPI specification together with an interactive Swagger UI, allowing every endpoint to be explored and tested directly from the browser.

#### Request body
```json
{
  "image": "string"
}
```

#### Example request:
```json
{
  "image": "examples/images/dog_and_person.jpg"
}
```

#### Example using curl
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/inference' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "image": "examples/images/dog_and_person.jpg"
}'
```

#### Example response:
```json
{
  "status": "success",
  "message": "Inference completed successfully.",
  "data": {
    "output_directory": "outputs/predict/dog_and_person.jpg"
  }
}
```

### HTTP Status Codes

| Code | Description |
|-----:|-------------|
| 200 | Request completed successfully |
| 400 | Invalid request payload |
| 404 | Requested image not found |
| 500 | Internal server error |

#### Example error
```json
{
    "status": "error",
    "message": "Image not found: examples/images/dog_an_person.jpg",
    "data": null
}
```

## Pipeline
---

```
   Image
     ↓
   Loader
     ↓
Preprocessor
     ↓
   YOLO11
     ↓
Postprocessor
     ↓
   Result
```

## Architecture
---

```
        Vision Pipeline
              │
  ┌───────────┴─────────────┐
  │                         │
 CLI                    REST API
  │                         │
  └───────────┬─────────────┘
              │
     Inference Service
              │
            YOLO11
```

## Documentation
---

For more details about the system architecture, design decisions and project roadmap, see [`docs/architecture.md`](./docs/architecture.md).

## Demo
---

![Inference](images/demo_inference.png)
*Figure: Object detection performed by Vision Pipeline using `YOLO11m`.*

## Project Status
---

- ✅ FastAPI REST API
- ✅ OpenAPI / Swagger UI
- ✅ Dockerized environment
- ✅ YOLO11 inference
- ✅ YAML configuration
- ✅ Application logging
- ✅ CLI interface
- ✅ Modular project architecture
- ⬜ ONNX Runtime backend
- ⬜ TensorRT backend

## Contact me
---

- **Author:** Eduardo de Jesús Dávila Meza, Ph.D.
- **LinkedIn:** [EduardoDavilaMeza](https://www.linkedin.com/in/eduardodavilameza/)
- **GitHub**: [eDavila-DrRaccoon](https://github.com/eDavila-DrRaccoon)