import board
import time
import adafruit_dht
import paho.mqtt.client as mqtt


broker = "10.0.0.36"
topic = "sensor/data"
feedback = "sensor/feedback"


dht_device = adafruit_dht.DHT11(board.D4, use_pulseio=False)


def on_connect(client, userdata, flags, rc):
    print("Connected to broker with code", rc)
    client.subscribe(feedback)


def on_message(client, userdata, msg):
    feedback = msg.payload.decode()
    print(f"Received feedback: {feedback}")
    latency = time.time() - start_time
    print(f"Fog Latency: {latency:.4f} seconds\n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883,60)
client.loop_start()


while True:
    try:
        start_time = time.time()
        temperature = dht_device.temperature
        payload = f"Temp: {temperature}°C"
        print(f"Publishing: {payload}")
        client.publish(topic, payload)
    except RuntimeError as e:
        time.sleep(1)
    time.sleep(5)  # Publish every 5 seconds
