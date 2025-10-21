import network, time
from machine import Pin
import dht
from umqtt.simple import MQTTClient

AIO_USERNAME = "**********"
AIO_KEY = "***********"
BROKER = "io.adafruit.com"

TEMP_FEED = f"{AIO_USERNAME}/feeds/temperature"
CONTROL_FEED = f"{AIO_USERNAME}/feeds/control"

sensor = dht.DHT11(Pin(4))
client = MQTTClient("esp32_client", BROKER, user=AIO_USERNAME, password=AIO_KEY)
client.connect()

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    payload = f"Temp:{temp}C, Humidity:{hum}%"
    print("Sending to Cloud:", payload)
    client.publish(TEMP_FEED.encode(), payload.encode())
    time.sleep(10)
