FROM python:3.13-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Only copy the necessary files to install the package
COPY pyproject.toml .
COPY src/ src/

RUN pip install -e .

# Copy the rest of the files
COPY scripts/ scripts/
COPY configs/ configs/
COPY examples/ examples/
COPY README.md .

# CMD ["python3", "scripts/inference.py", "examples/images/dog_and_person.jpg"]
# CMD ["python3", "-m", "scripts.inference", "examples/images/dog_and_person.jpg"]
CMD ["uvicorn", "vision_pipeline.api.app:app", "--host", "0.0.0.0", "--port", "8000"]