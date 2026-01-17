# 🚀 IoT App

Dummy Modbus TCP temperature sensor for IoT testing.

---

## Project Setup

This project uses **[`uv`](https://github.com/astral-sh/uv)** for dependency management and a **Makefile** to simplify common commands.

### Prerequisites

- Python **3.13+**
- [`uv`](https://github.com/astral-sh/uv)

---

## Initial Setup

- **_Makefile Command Reference_**

```bash
➜ make help

Available commands:
  make venv        Create virtual environment
  make install     Install dependencies
  make run-modbus  Run Modbus TCP server
  make run-mqtt    Run MQTT publisher
  make run-client  Run Modbus TCP client
  make lint        Run ruff lint checks
  make format      Format code (black + isort)
  make fix         Auto-fix lint + format
  make clean       Remove virtual environment
```

1. **Create a virtual environment**

```bash
make venv
```

2. **Activate the virtual environment**

- _Linux / macOS_

```bash
source .venv/bin/activate
```

- _Windows (PowerShell)_

```bash
.venv\Scripts\Activate.ps1
```

3. **Install dependencies**

```bash
make install
```

This will create a `.venv` directory and install all required dependencies using `uv`.

---

## Running the Application

This project consists of three main components:

- **Modbus TCP Server** – Simulates a temperature sensor
- **MQTT Publisher** – Publishes temperature data to an MQTT broker
- **Modbus TCP Client** – Reads data from the Modbus server

---

### 1. Start the Modbus TCP Server

```bash
make run-modbus
```

The Modbus server will start and listen on **TCP port 5020**.

---

### 2. Start the MQTT Publisher (Optional)

```bash
make run-mqtt
```

The MQTT publisher connects to a broker at:

```
localhost:1883
```

> ⚠️ Make sure an MQTT broker (e.g. Mosquitto) is running locally.

---

### 3. Run the Modbus TCP Client

```bash
make run-client
```

The client connects to the Modbus server, reads the temperature data, and prints it to the console.

---

## Code Quality & Formatting

This project uses:

- **Ruff** – Linting
- **Black** – Code formatting
- **isort** – Import sorting

### Run lint checks

```bash
make lint
```

### Format code

```bash
make format
```

### Auto-fix lint and formatting issues

```bash
make fix
```

---

## Notes

- Development tools (`ruff`, `black`, `isort`) are **dev dependencies**
- Docker images install **production dependencies only**
- Modbus TCP server binds to `0.0.0.0` and is accessible via port `5020`
