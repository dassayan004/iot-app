from pymodbus.client import ModbusTcpClient
import time

MODBUS_HOST = "localhost"
MODBUS_PORT = 5020
SLAVE_ID = 1

client = ModbusTcpClient(host=MODBUS_HOST, port=MODBUS_PORT, timeout=3)

print("🔌 Connecting to Modbus server...")

if client.connect():
    try:
        while True:
            response = client.read_holding_registers(
                address=0,
                count=2,
                device_id=SLAVE_ID,
            )

            if response.isError():
                print(f"❌ Modbus Error: {response}")
            else:
                temperature = response.registers[0] / 10.0
                status = response.registers[1]

                print(
                    f"🌡️ Temp: {temperature:.1f} °C | Status: {'OK' if status == 1 else 'FAULT'}"
                )

            time.sleep(2)
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
    finally:
        client.close()
else:
    print("❌ Connection Failed")
