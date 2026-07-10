import argparse
from pathlib import Path

from ultralytics import YOLO

from vision_pipeline.config.loader import load_config
from vision_pipeline.utils.logging import configure_logger

def main() -> list: # List or None
    parser = argparse.ArgumentParser(description="Run YOLO11 inference on an image.")
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()

    image_path = Path(args.image)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    config = load_config()

    logger = configure_logger(config["logging"]["level"])
    logger.info("Loading model: %s", config["model"]["weights"])
    
    model = YOLO(config["model"]["weights"])

    logger.info("Running inference...")

    results = model.predict(
        source=str(image_path),
        conf=config["inference"]["confidence"],
        device=config["inference"]["device"],
        save=config["output"]["save"],
        project=config["output"]["directory"],
        name=config["output"]["name"],
        exist_ok=True,
    )

    logger.info("Results saved to %s", results[0].save_dir)
    logger.info("Finished successfully.")
    
    # return results

if __name__ == "__main__":
    main()