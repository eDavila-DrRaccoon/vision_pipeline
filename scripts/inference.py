from pathlib import Path
import argparse

from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="Run YOLO11 inference on an image.")
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()

    image_path = Path(args.image)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    model = YOLO("yolo11n.pt")

    results = model.predict(
        source=str(image_path),
        save=True,
        project="outputs",
        name="predict",
        exist_ok=True,
    )

    print(f"Inference completed. Results saved to {results[0].save_dir}")
    
    return results

if __name__ == "__main__":
    main()