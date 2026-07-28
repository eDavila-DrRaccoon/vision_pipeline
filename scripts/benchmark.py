import statistics
import time
from pathlib import Path

import psutil

from vision_pipeline.benchmark.hardware import get_cpu_name, get_gpu_name, get_total_ram
from vision_pipeline.benchmark.report import export_benchmark_report
from vision_pipeline.config.loader import load_config
from vision_pipeline.pipelines.inference import run_inference

IMAGE = "examples/images/books.jpg"
ITERATIONS = 10

def main():
    print("\n[vision_pipeline] [BENCHMARK] Warming-up...")
    
    run_inference(IMAGE, export=False)

    print(f"[vision_pipeline] [BENCHMARK] Running {ITERATIONS} benchmark iterations...\n")

    timings = []

    process = psutil.Process()

    for _ in range(ITERATIONS):
        start = time.perf_counter()

        run_inference(IMAGE, export=False)

        end = time.perf_counter()

        timings.append(end - start)

    config = load_config()
    average_latency = statistics.mean(timings)

    benchmark = {
        "backend": "PyTorch",
        "device": config["inference"]["device"],
        "model": config["model"]["weights"],
        "model_size_mb": round(Path(config['model']['weights']).stat().st_size / (1024 ** 2), 2),
        "image": IMAGE,
        "iterations": ITERATIONS,
        "average_inference_s": round(average_latency, 4),
        "fps": round(1 / average_latency, 2),
        "memory_mb": round(process.memory_info().rss / 1024**2, 2),
        "hardware": {
            "cpu": get_cpu_name(),
            "gpu": get_gpu_name(),
            "ram": get_total_ram(),
        },
    }

    print("[vision_pipeline] [BENCHMARK] Benchmark completed successfully.\n")
    print("====== Benchmark Results ======")
    print(f"Device            : {benchmark['device']}")
    print(f"Model             : {benchmark['model']}")
    print(f"Model Size        : {benchmark['model_size_mb']:.2f} MB")
    print(f"Average inference : {benchmark['average_inference_s']:.4f} s")
    print(f"FPS               : {benchmark['fps']:.2f}")
    print(f"RAM Usage         : {benchmark['memory_mb']:.2f} MB")

    report = export_benchmark_report(benchmark)

    print(f"\n[vision_pipeline] [BENCHMARK] Report exported to: {report}")

if __name__ == "__main__":
    main()