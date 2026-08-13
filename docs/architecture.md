# Vision Pipeline Architecture v1

## 1. Objective
---

Vision Pipeline is a modular computer vision inference framework designed to demonstrate production-oriented software engineering practices for AI applications.

The primary goals of this project are:

- Modular architecture
- Reusable components
- Docker-first deployment
- Clean APIs
- Multiple inference backends
- Professional documentation
- Easy migration to optimized runtimes (ONNX Runtime, TensorRT)

## 2. MVP Data Flow
---

```
   Image
     ↓
   Loader
     ↓
Preprocessor
     ↓
   Model
     ↓
Postprocessor
     ↓
   Result
```

The MVP focuses on image inference from local image paths (on the server) or uploaded images (`application/json` + `multipart/form-data` via API).

## 3. REST Layer
---

```
       Client
         ↓
  FastAPI Router
         ↓
Inference Pipeline
         ↓
       YOLO11
         ↓
     JSON Response
```

The REST layer exposes the inference pipeline through FastAPI endpoints. Request validation is performed with Pydantic models, while responses follow a consistent JSON schema to simplify client integration and future API evolution.

## 4. Project Structure
---

```
vision_pipeline/
├── configs
│   └── default.yaml
├── docker
├── docs
│   ├── architecture.md
│   ├── benchmark.md
│   ├── openapi.json
│   ├── openapi.md
│   └── testing.md
├── examples
│   └── images
├── images
├── outputs
│   └── predict
├── reports
│   └── benchmarks
│       ├── benchmark_<timestamp>.json
│       └── benchmark_history.csv
├── scripts
│   ├── benchmark.py
│   ├── export_openapi.py
│   └── inference.py
├── src
│   └── vision_pipeline
│       ├── api
│       │   ├── app.py
│       │   ├── exceptions.py
│       │   ├── handlers.py
│       │   ├── responses.py
│       │   ├── routes.py
│       │   └── schemas.py
│       ├── backends
│       ├── benchmark
│       │   ├── hardware.py
│       │   └── report.py
│       ├── config
│       │   └── loader.py
│       ├── io
│       │   ├── image_validation.py
│       │   ├── outputs.py
│       │   └── uploads.py
│       ├── models
│       ├── pipelines
│       │   └── inference.py
│       ├── utils
│       │   └── logging.py
│       └── visualization
├── tests
│   ├── integration
│   │   └── test_api.py
│   ├── resources
│   │   └── dummy.txt
│   ├── unit
│   │   ├── test_api_response.py
│   │   ├── test_config.py
│   │   ├── test_hardware.py
│   │   └── test_pipeline.py
│   └── conftest.py
├── tmp
│   └── uploads
├── videos
├── weights
│   └── yolo11m.pt
├── _config.yml
├── compose.yaml
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── pytest.ini
├── README.md
└── requirements.txt
```

## 5. Technology Stack
---

| Component | Selected Technology |
|:---------:|:-------------------:|
| Language | Python |
| Deep Learning | PyTorch |
| Initial Model | YOLO11 |
| REST API | FastAPI |
| Deployment | Docker + Docker Compose |
| Configuration | YAML |
| Response Format | Uniform JSON contract |
| Benchmarking | JSON reports + CSV history |
| Future Inference | ONNX Runtime, TensorRT |

## 6. Roadmap
---

### Phase 1

- Docker environment
- YOLO11 inference
- Local CLI

### Phase 2

- REST API
- OpenAPI
- JSON schemas

### Phase 3

- Benchmark infrastructure
- Benchmark report export
- Benchmark history

### Phase 4

- ONNX Runtime backend
- TensorRT backend
- Backend performance comparison
- Video inference
- Multi-model support
- Production deployment

## Related Documentation
---

- [Benchmark](./benchmark.md)  
- [OpenAPI](./openapi.md)  
- [Testing](./testing.md)  

---

[Back to the Main Page](../README.md)