FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY src ./src
COPY README.md .

EXPOSE 5020

CMD ["uv", "run", "--no-sync", "--no-dev", "src/modbus_server.py"]
