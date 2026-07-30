import json
from pathlib import Path

from vision_pipeline.api.app import app
from vision_pipeline.utils.logging import configure_logger


logger = configure_logger(level="INFO", name="vision_pipeline.openapi.export")

def main() -> None: # output: Path = Path("docs/openapi.json") -> Path
    output = Path("docs/openapi.json")
    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(
        json.dumps(app.openapi(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    logger.info(f"OpenAPI specification exported to: {output}")

    # return output


if __name__ == "__main__":
    main()