import statistics
import time
from pathlib import Path
import psutil
from ultralytics import YOLO
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
        "device": config["inference"]["device"],
        "model": config["model"]["weights"],
        "size": Path(config["model"]["weights"]).stat().st_size / (1024 ** 2),
        "average_latency": average_latency,
        "fps": 1 / average_latency,
        "memory": process.memory_info().rss / 1024**2
    }

    print("[vision_pipeline] [BENCHMARK] Benchmark completed successfully.\n")
    print("====== Benchmark Results ======")
    print(f"Device            : {benchmark['device']}")
    print(f"Model             : {benchmark['model']}")
    print(f"Average inference : {benchmark['average_latency']:.3f} s")
    print(f"FPS               : {benchmark['fps']:.2f}")
    print(f"RAM Usage         : {benchmark['memory']:.2f} MB")
    print(f"Model Size        : {benchmark['size']:.2f} MB")

if __name__ == "__main__":
    main()