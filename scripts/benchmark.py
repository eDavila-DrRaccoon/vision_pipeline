import statistics
import time
from pathlib import Path

import psutil

from vision_pipeline.benchmark.hardware import get_cpu_name, get_gpu_name, get_total_ram
from vision_pipeline.benchmark.report import export_benchmark_report
from vision_pipeline.config.loader import load_config
from vision_pipeline.pipelines.inference import run_inference
from vision_pipeline.utils.logging import configure_logger

IMAGE = "examples/images/books.jpg"
ITERATIONS = 10

logger = configure_logger(level="INFO", name="vision_pipeline.benchmark")

def main():
    logger.info("Warming-up...")
    
    run_inference(IMAGE, export=False)

    logger.info(f"Running {ITERATIONS} benchmark iterations on {IMAGE}...\n")

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
        "timestamp": '', # It is filled in by the export_benchmark_report function
        "backend": "PyTorch",
        "device": config["inference"]["device"],
        "hardware": {
                    "cpu": get_cpu_name(),
                    "gpu": get_gpu_name(),
                    "ram_gb": get_total_ram(),
                },
        "model": config["model"]["weights"],
        "model_size_mb": round(Path("weights/" + config['model']['weights']).stat().st_size / (1024 ** 2), 2),
        "iterations": ITERATIONS,
        "image": IMAGE,
        "average_inference_s": round(average_latency, 4),
        "fps": round(1 / average_latency, 2),
        "memory_mb": round(process.memory_info().rss / 1024**2, 2)
    }

    logger.info("Benchmark completed successfully.\n")
    logger.info("====== Benchmark Results ======")
    logger.info(f"Device            : {benchmark['device']}")
    logger.info(f"Model             : {benchmark['model']}")
    logger.info(f"Model Size        : {benchmark['model_size_mb']:.2f} MB")
    logger.info(f"Average inference : {benchmark['average_inference_s']:.4f} s")
    logger.info(f"FPS               : {benchmark['fps']:.2f}")
    logger.info(f"RAM Usage         : {benchmark['memory_mb']:.2f} MB")

    report = export_benchmark_report(benchmark)

    logger.info(f"Report exported to: {report}")
    logger.info(f"Report appended to: {report.parent / 'benchmark_history.csv'}")

if __name__ == "__main__":
    main()