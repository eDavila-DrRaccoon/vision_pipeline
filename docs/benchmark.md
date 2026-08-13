# Benchmark v1

## 1. Objective
---

This document establishes the initial performance baseline of Vision Pipeline using the current PyTorch inference backend and the YOLO11m model.

The collected metrics will serve as a reference for future comparisons against optimized inference backends such as ONNX Runtime and TensorRT.

## 2. Test Configuration
---

| Parameter | Value |
|:---------:|:-----:|
| Backend | PyTorch |
| Device | CPU |
| Model | YOLO11m |
| Model size | 38.80 MB |
| Iterations | 10 |
| Warm-up | 1 iteration (excluded from results) |
| Input image | `examples/images/books.jpg` |

## 3. Hardware
---

| Component | Value |
|:---------:|:-----:|
| CPU | Intel® Core™ i7-9700K @ 4.90 GHz |
| GPU | NVIDIA GeForce RTX 3070 LHR *(not used in this benchmark)* |
| RAM | 64 GB DDR4 |
| Operating System | Ubuntu 26.04 LTS (Resolute Raccoon) |
| Kernel | Linux 7.0.0-28-generic |
| Python | 3.14 |

## 4. Methodology
---

The benchmark measures the **end-to-end execution time** of the Vision Pipeline inference function.

Each iteration performs the following operations:

```
  Input image
       ↓
 Image validation
       ↓
 YOLO11 inference
       ↓
Results generation
       ↓
 Return to caller
```

To obtain more representative measurements:

- the YOLO model is loaded only once before benchmarking;
- one warm-up inference is executed before collecting measurements;
- prediction image export is disabled;
- the average execution time is computed over ten consecutive iterations.

Unlike the internal timing reported by Ultralytics, this benchmark measures the total execution time perceived by the application.

## 5. Results
---

The following values represent the **baseline benchmark selected for the v1.0.0 release documentation** using the test configuration and reference hardware described above.

| Metric | Value |
|:------:|:-----:|
| Average inference time | **131.2 ms** |
| Throughput | **7.62 FPS** |
| RAM usage | **979.26 MB** |

#### (Example) Terminal output:

```text
[vision_pipeline.benchmark] [INFO] ====== Benchmark Results ======
[vision_pipeline.benchmark] [INFO] Device            : cpu
[vision_pipeline.benchmark] [INFO] Model             : yolo11m.pt
[vision_pipeline.benchmark] [INFO] Model Size        : 38.80 MB
[vision_pipeline.benchmark] [INFO] Average inference : 0.1312 s
[vision_pipeline.benchmark] [INFO] FPS               : 7.62
[vision_pipeline.benchmark] [INFO] RAM Usage         : 979.26 MB
[vision_pipeline.benchmark] [INFO] Report exported to: reports/benchmarks/benchmark_2026-07-28_18-20-32.json
[vision_pipeline.benchmark] [INFO] Report appended to: reports/benchmarks/benchmark_history.csv
```

## 6. Benchmark Script
---

The benchmark can be executed with:

```bash
python scripts/benchmark.py
```

The script automatically:

- loads the configured model;
- performs one warm-up inference;
- executes multiple benchmark iterations;
- computes the average inference time;
- estimates throughput (FPS);
- reports memory usage and model size;
- exports a timestamped JSON report;
- appends the execution summary to the benchmark history CSV.

## 7. Benchmark Reports
---

Each benchmark execution automatically generates two report files under:

```text
reports/benchmarks/
```

Each benchmark execution produces two report formats:

- **JSON**, containing the complete benchmark metadata and metrics.
- **CSV**, which appends a summary entry to facilitate historical comparisons.

The exported reports provide a reproducible record of every benchmark execution, enabling historical comparisons across different hardware configurations, inference backends and model versions.

#### Example JSON structure:

```json
{
      "timestamp": "2026-07-28T18:20:32",
      "backend": "PyTorch",
      "device": "cpu",
      "hardware": {
            "cpu": "Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz",
            "gpu": "NVIDIA GeForce RTX 3070",
            "ram_gb": 60.45
      },
      "model": "yolo11m.pt",
      "model_size_mb": 38.8,
      "iterations": 10,
      "image": "examples/images/books.jpg",
      "average_inference_s": 0.1312,
      "fps": 7.62,
      "memory_mb": 979.26
}
```

#### Example CSV structure:

| timestamp	| backend |	model | device | average_inference_s | fps | memory_mb |
|:---------:|:-------:|:-----:|:------:|:-------------------:|:---:|:---------:|
| 2026-07-28T18:20:32 |	PyTorch | yolo11m.pt | cpu | 0.1312 | 7.62 | 979.26 |

## 8. Metrics
---

| Metric | Description |
|:------:|:-----------:|
| Backend | Inference engine used during the benchmark (PyTorch, ONNX Runtime or TensorRT). |
| Device | Execution target (CPU or GPU). |
| Average inference | Mean execution time across all benchmark iterations. |
| FPS | Estimated throughput computed as the inverse of the average inference time. |
| RAM usage | Resident memory consumed by the benchmark process. |

## 9. Comparing Benchmarks
---

For meaningful comparisons, benchmark executions should be performed under identical conditions.

Recommendations:

- use the same input image;
- use the same number of iterations;
- execute one backend at a time;
- avoid background processes that may affect performance;
- compare the exported JSON or CSV reports instead of console output.
- keep the same YOLO model weights when comparing inference backends.

This methodology provides reproducible measurements across different software and hardware configurations.

## 10. Current Limitations
---

This first benchmark intentionally focuses on establishing a reproducible baseline.

Current limitations include:

- CPU execution only;
- single-image inference;
- batch size of one;
- no GPU measurements;
- no peak memory tracking;
- no latency distribution (minimum, maximum or standard deviation).
- benchmark executed on a single hardware platform.

These aspects will be incorporated in future benchmarking iterations as additional inference backends are implemented.

## 11. Future Benchmark Roadmap
---

The current benchmarking infrastructure has been designed to support multiple inference backends.

| Backend | Planned |
|:-------:|:-------:|
| PyTorch | ✅ |
| ONNX Runtime | ⬜ |
| TensorRT | ⬜ |

Future benchmark versions will also compare:

- CPU versus GPU execution;
- different YOLO model variants;
- multiple batch sizes;
- latency distribution;
- peak memory consumption;
- multiple input images.

## 12. Benchmark Image
---

![Benchmark inference](../images/demo_benchmark.png)
**Figure:** *Benchmark image processed using the PyTorch backend and `YOLO11m`.*

## Related Documentation
---

- [Architecture](./architecture.md)  
- [OpenAPI](./openapi.md)  
- [Testing](./testing.md)  

---

[Back to the Main Page](../README.md)