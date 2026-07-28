import csv
import json
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports/benchmarks")
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

CSV_FILE = REPORTS_DIR / "benchmark_history.csv"

def export_benchmark_report(benchmark: dict) -> Path:
    """
    Export benchmark results to both JSON and CSV formats.

    Parameters
    ----------
    benchmark : dict
        Benchmark metrics and metadata.

    Returns
    -------
    Path
        Path to the generated JSON report.
    """

    timestamp = datetime.now()

    benchmark["timestamp"] = timestamp.isoformat(timespec="seconds")

    filename = f"benchmark_{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}"

    json_path = REPORTS_DIR / f"{filename}.json"

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(
            benchmark,
            file,
            indent=4,
        )

    csv_exists = CSV_FILE.exists()

    with CSV_FILE.open(
        "a",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.writer(file)

        if not csv_exists:
            writer.writerow([
                "timestamp",
                "backend",
                "model",
                "device",
                "average_inference_s",
                "fps",
                "memory_mb",
            ])

        writer.writerow([
            benchmark["timestamp"],
            benchmark["backend"],
            benchmark["model"],
            benchmark["device"],
            benchmark["average_inference_s"],
            benchmark["fps"],
            benchmark["memory_mb"],
        ])

    return json_path