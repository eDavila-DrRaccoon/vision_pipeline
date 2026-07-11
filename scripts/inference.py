import argparse
from vision_pipeline.pipelines.inference import run_inference

def main():
    parser = argparse.ArgumentParser(description="Run inference on an image using the vision pipeline.")
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()

    run_inference(args.image)

if __name__ == "__main__":
    main()