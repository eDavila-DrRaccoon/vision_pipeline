FROM python:3.13-slim

WORKDIR /workspace

COPY . .

CMD ["python3", "-c", "print('Vision Pipeline')"]