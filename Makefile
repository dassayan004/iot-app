.PHONY: help venv install run-modbus run-mqtt run-client lint format fix clean

help:
	@echo "Available commands:"
	@echo "  make venv        Create virtual environment"
	@echo "  make install     Install dependencies"
	@echo "  make run-modbus  Run Modbus TCP server"
	@echo "  make run-mqtt    Run MQTT publisher"
	@echo "  make run-client  Run Modbus TCP client"
	@echo "  make lint        Run ruff lint checks"
	@echo "  make format      Format code (black + isort)"
	@echo "  make fix         Auto-fix lint + format"
	@echo "  make clean       Remove virtual environment"

venv:
	uv venv

install:
	uv sync

run-modbus:
	uv run src/modbus_server.py

run-mqtt:
	uv run src/mqtt_server.py

run-client:
	uv run client.py

lint:
	uv run ruff check .

format:
	uv run black .
	uv run isort .

fix:
	uv run ruff check . --fix
	uv run black .
	uv run isort .

clean:
	rm -rf .venv
