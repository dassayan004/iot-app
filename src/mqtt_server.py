import json
import random
import time
import signal

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
TOPIC = "iot/temperature"

# Global flag for graceful exit
running = True


def signal_handler(sig, frame):
    global running
    print("\n🛑 Stopping MQTT dummy...")
    running = False


def start_mqtt_publisher() -> None:
    global running

    print(f"🟢 MQTT dummy running on TCP {MQTT_BROKER}:{MQTT_PORT}")

    client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)

    # Retry until broker is up
    while True:
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
            break
        except ConnectionRefusedError:
            print("⏳ MQTT broker not ready, retrying...")
            time.sleep(2)

    time.sleep(0.5)

    while running:
        temp = round(random.uniform(20.0, 35.0), 1)
        payload = {"temperature": temp, "unit": "C"}

        client.publish(TOPIC, json.dumps(payload))
        print(f"[MQTT] Published → {payload}")
        time.sleep(2)

    print("✅ MQTT dummy stopped.")


if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    start_mqtt_publisher()
