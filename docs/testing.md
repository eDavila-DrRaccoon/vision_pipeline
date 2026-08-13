# API Testing v1

The integration suite uses FastAPI's `TestClient` to exercise the REST layer without requiring an external server process.

## 1. Objective
---

Vision Pipeline includes both unit tests and integration tests.

Vision Pipeline can be exercised through both the command-line interface and the REST API.

The CLI provides a direct way to execute the inference pipeline locally, while the integration suite validates the REST API from a client perspective.

### Unit tests

Unit tests validate individual modules in isolation, ensuring that each component behaves correctly without depending on the REST API or external services.

Current unit tests cover examples such as:

- response models
- configuration loading
- inference pipeline
- hardware utilities

### Integration tests

Integration tests validate the complete FastAPI request lifecycle.

Instead of testing isolated functions, they execute HTTP requests against the application using FastAPI's `TestClient` and verify that the API behaves as expected from a client perspective.

## 2. Running Tests
---

Run the complete test suite:

```bash
pytest -vv
```

Run only the integration tests:

```bash
pytest -vv tests/integration
```

Run only the unit tests:

```bash
pytest -vv tests/unit
```

## 3. Covered Scenarios
---

Current integration tests validate:

- successful path-based inference
- successful upload inference
- missing image (404)
- unsupported image extension (400)
- invalid MIME type (400)
- REST response contract
- response status codes
- JSON schema consistency

## 4. Future Work
---

Future testing stages will include:

- Docker integration tests
- end-to-end deployment validation
- benchmark regression tests
- performance tests
- load tests
- GPU-specific tests
- OpenAPI contract validation

## Related Documentation
---

- [Architecture](./architecture.md) 
- [Benchmark](./benchmark.md)  
- [OpenAPI](./docs/openapi.md)  

---

[Back to the Main Page](../README.md)