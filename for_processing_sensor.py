import network, time
from machine import Pin
import dht
from umqtt.simple import MQTTClient

BROKER = "192.x.x.x"  # Raspberry Pi IP
TOPIC = b"sensor/data"
CLIENT_ID = b"esp32_sensor"

sensor = dht.DHT11(Pin(4))

client = MQTTClient(CLIENT_ID, BROKER)
client.connect()

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    payload = f"Temp:{temp}C, Humidity:{hum}%"
    print("Publishing:", payload)
    client.publish(TOPIC, payload)
    time.sleep(5)
