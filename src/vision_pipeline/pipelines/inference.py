from pathlib import Path
from ultralytics import YOLO
from vision_pipeline.config.loader import load_config
from vision_pipeline.utils.logging import configure_logger

def run_inference(image_path: str): # List or None
    image = Path(image_path)

    if not image.exists():
        raise FileNotFoundError(image)

    config = load_config()
    
    logger = configure_logger(config["logging"]["level"])
    logger.info("Loading model: %s", config["model"]["weights"])

    model = YOLO(config["model"]["weights"])

    logger.info("Running inference...")

    results = model.predict(
        source=str(image),
        conf=config["inference"]["confidence"],
        device=config["inference"]["device"],
        save=config["output"]["save"],
        project=config["output"]["directory"],
        name=config["output"]["name"],
        exist_ok=True,
    )

    logger.info("Results saved to %s", results[0].save_dir)
    logger.info("Finished successfully.")

    return results