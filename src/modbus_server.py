import threading
import time
import random
from pymodbus.server import StartTcpServer
from pymodbus.datastore import (
    ModbusServerContext,
    ModbusDeviceContext,
    ModbusSequentialDataBlock,
)


MODBUS_PORT = 5020
SLAVE_ID = 1

hr_block = ModbusSequentialDataBlock(0, [250, 1] + [0] * 8)
store = ModbusDeviceContext(hr=hr_block)
context = ModbusServerContext(devices={SLAVE_ID: store}, single=False)


def simulate_temperature():

    while True:
        temp = round(random.uniform(20.0, 35.0), 1)
        store.setValues(3, 0, [int(temp * 10), 1])
        print(f"[Modbus] Temperature updated → {temp} °C")
        time.sleep(2)


def start_modbus_server() -> None:
    print(f"🟢 Modbus TCP running on port {MODBUS_PORT}")
    threading.Thread(
        target=simulate_temperature,
        daemon=True,
    ).start()

    StartTcpServer(context, address=("0.0.0.0", MODBUS_PORT))


if __name__ == "__main__":
    start_modbus_server()
