# IoT Temperature Sensor Node
## Overview
This project demonstrates how fog and cloud computing process IoT sensor data differently in terms of latency and response time.
A DHT11 sensor connected to an ESP32 collects temperature and humidity data and sends it to a Raspberry Pi acting as a fog node (local processing) and to a cloud server (Adafruit IO) for remote processing.

### Workflow
* The ESP32 reads data from the DHT11 sensor.
* It publishes the readings to the Raspberry Pi (Fog Node) via MQTT.
* The Fog Node locally processes the data, sends a feedback message (e.g., “Too cold, turn on heater”), and forwards the data to the cloud.
* The Cloud (Adafruit IO) stores the readings, allows remote access, and may send cloud-level feedback back to the system.

## Materials Used
* ESP32-WROOM-32E Dev Board
* DHT11 Sensor
* Fog Node (Raspberry Pi)
* Custom PCB for connecting DHT11 to ESP32-WROOM-32E Dev Board
* MQTT Broker

## Results
Fog processing provides quicker response times since computations occur closer to the sensor, while cloud processing offers better scalability and data visibility at the cost of higher latency.

