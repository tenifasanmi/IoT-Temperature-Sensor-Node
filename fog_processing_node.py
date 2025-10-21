import paho.mqtt.client as mqtt

topic = "sensor/data"
feedback = "sensor/feedback"

ideal_temp = 19.0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"Received temperature: {payload}")
    
    if "Temp:" in payload:
        temp_str = payload.split("Temp: ")[1].split("°")[0]
        try:
            temperature = float(temp_str)

            # Decision logic
            if temperature < 22:
                feedback_msg = "Too cold, turn on heater"
            elif temperature > 22:
                feedback_msg = "Too warm, turn on fan"
            else:
                feedback_msg = "Temperature is optimal"

            print(f"Sending feedback: {feedback_msg}")
            client.publish(feedback, feedback_msg)
        except ValueError:
            print("Error parsing temperature.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
