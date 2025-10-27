import board
import time
import adafruit_dht
import requests
import paho.mqtt.client as mqtt


AIO_USERNAME = "******"
AIO_KEY = "******"
temp_feed = f"username/feeds/temperature"
control_feed = f"username/feeds/control"
broker = "io.adafruit.com"


dht_device = adafruit_dht.DHT11(board.D4, use_pulseio=False)


client = mqtt.Client()
client.username_pw_set(AIO_USERNAME, AIO_KEY)
client.connect(broker, 1883,60)


def on_message(client, userdata, message):
    print(f"Received from cloud: {message.payload.decode()}")
    cloud_latency = measure_latency(start_time, "Cloud")
    
client.on_message = on_message
client.subscribe(control_feed)
client.loop_start()


def measure_latency(start_time, system_type):
    latency = time.time() - start_time
    print(f"{system_type} Latency: {latency:.4f} seconds\n")
    return latency


while True:
    try:
        start_time = time.time()
        temperature = dht_device.temperature
        payload = f"Temp: {temperature}°C"
        print(f"Sending: {payload}")
        client.publish(temp_feed, payload)
        
    except RuntimeError as e:
        time.sleep(1)
    time.sleep(10)  # Publish every 5 seconds
