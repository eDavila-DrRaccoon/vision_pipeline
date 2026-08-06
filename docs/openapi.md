# OpenAPI Specification v1

## 1. Objective
---

Vision Pipeline exposes its REST API through FastAPI, which automatically generates an OpenAPI specification describing the application contract.

The exported specification provides a machine-readable description of every endpoint, request body, response schema and supported HTTP status code.

Maintaining this contract separately facilitates integrations with external tools while ensuring that the REST API remains consistently documented.

## 2. Export
---

The OpenAPI specification can be regenerated at any time by executing:

```bash
python scripts/export_openapi.py
```

This command loads the FastAPI application, generates the OpenAPI schema and exports it as a JSON document.

The generated file can be committed to the repository to provide a versioned API contract alongside the source code.

## 3. Location
---

The exported specification is stored at:

```text
docs/openapi.json
```

This file should be regenerated whenever endpoints, request models, response models or API metadata are modified.

## 4. Uses
---

The exported OpenAPI specification can be used for:

- interactive API documentation through Swagger UI;
- validating the REST contract during development;
- importing the API into Postman;
- automatic SDK generation for multiple programming languages;
- generating external documentation.

Using a standardized API contract improves interoperability and simplifies client integration.

## 5. Specification Contents
---

The exported OpenAPI document includes:

- API metadata;
- available endpoints;
- request and response schemas;
- HTTP methods;
- response status codes;
- OpenAPI version information.

This information is generated automatically from the FastAPI application and remains synchronized with the implemented REST API.

The exported specification includes both inference endpoints:

| Endpoint | Input | Intended use |
| :------: | :---: | :----------: |
| `POST /inference/path` | `application/json` | Local development, automated testing and benchmarking |
| `POST /inference/upload` | `multipart/form-data` | Web applications, mobile clients and third-party services |


Although the request formats differ, both endpoints delegate inference to the same pipeline implementation and expose an identical response schema. This design keeps the REST contract consistent while supporting multiple image input methods.

## 6. Future Work
---

Future improvements include:

- API versioning;
- automatic specification generation during CI;
- automatic publication of the specification through GitHub Pages;
- generation of client SDKs;
- automated contract validation.

---

### Related Documentation

- [Architecture](../docs/architecture.md)  
- [Benchmark](../docs/benchmark.md)  
- [Testing](../docs/testing.md)  

---

[Back to the Main Page](../README.md)