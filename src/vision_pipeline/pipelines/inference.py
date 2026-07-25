from pathlib import Path
from ultralytics import settings, YOLO
from vision_pipeline.config.loader import load_config
from vision_pipeline.io.outputs import export_prediction
from vision_pipeline.utils.logging import configure_logger

PROJECT_ROOT = Path(__file__).resolve().parents[3]

def run_inference(image_path: str) -> Path:
    """
    Run object detection on an image and export the prediction
    into the Vision Pipeline output directory.
    """

    # settings.reset()
    settings.update({
        "datasets_dir": str(PROJECT_ROOT / "datasets"),
        "weights_dir": str(PROJECT_ROOT / "weights"),
        "runs_dir": str(PROJECT_ROOT / "runs"),
    })

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
        project=config["output"]["root"],
        name=config["output"]["name"],
        exist_ok=True,
    )

    save_dir = Path(results[0].save_dir)
    generated_image = save_dir / image.name

    if not generated_image.exists():
        raise FileNotFoundError(
            f"Expected output image not found: {generated_image}"
        )

    final_output = export_prediction(
        generated_image=generated_image,
        output_root=config["output"]["root"],
        output_name=config["output"]["name"],
    )

    # a) results (results[0].save_dir) for the original save dir,
    # b) final_output for the new location
    logger.info("Results saved to %s", final_output)
    logger.info("Finished successfully.")

    return final_output