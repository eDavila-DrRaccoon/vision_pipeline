import argparse
from pathlib import Path

from ultralytics import YOLO

from vision_pipeline.config.loader import load_config

def main() -> list: # List or None
    parser = argparse.ArgumentParser(description="Run YOLO11 inference on an image.")
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()

    image_path = Path(args.image)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    config = load_config()
    
    model = YOLO(config["model"]["weights"])

    results = model.predict(
        source=str(image_path),
        conf=config["inference"]["confidence"],
        device=config["inference"]["device"],
        save=config["output"]["save"],
        project=config["output"]["directory"],
        name=config["output"]["name"],
        exist_ok=True,
    )

    print(f"Inference completed. Results saved to {results[0].save_dir}")
    
    # return results

if __name__ == "__main__":
    main()