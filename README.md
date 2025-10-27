# IoT Temperature Sensor Node
## Overview
This project demonstrates fog and cloud computing for IoT sensor data, differing in terms of latency and response time.
A DHT11 sensor connected to an ESP32 collects temperature and humidity data, and sends it to a Raspberry Pi acting as a fog node (local processing) or to a cloud server (Adafruit IO) for remote processing. For this project, I made use of Freenove's ESP32 WROOM Development Board. This choice was mainly due to its small size and wifi/Bluetooth capabilities. I couldn't find a footprint/symbol for this board online for use in my schematics, so I designed the PCB using a pin header connector to connect my board to the PCB. The pin headers correspond with the pins of the devboard and allow for connection between the board and the temperature sensor. The DHT11 can also be interchanged with the DHT22 temperature sensor, which offers higher accuracy and a wider temperature range, but is more costly.
Initially, this system was tested using a Raspberry Pi 4B as the sensor node and my local PC as the fog node for processing. Due to constraints in real-world applications, such as size, as well as the fact that this is a small-scale device which doesn't require all the functionalities of a Raspberry Pi 4B, this project was switched to an ESP32. For this project, the code was written in Python using the Raspberry Pi; however, I have decided to implement it in C for the ESP32. The functionality remains the same for both implementations.

## Raspberry Pi-based IoT Sensor Node
### Workflow
* The Raspberry Pi reads data from the DHT11 sensor.
* It publishes the readings to the PC (Fog Node) via MQTT.
* The Fog Node locally processes the data, sends a feedback message (e.g., “Too cold, turn on heater”), and forwards the data to the cloud.
* The Cloud (Adafruit IO) stores the readings, allows remote access, and sends cloud-level feedback back to the system.

### Materials Used
* Raspberry Pi 4B
* DHT11 Sensor
* Fog Node (Windows PC)
* Cloud Server (Adafruit IO)
* MQTT Broker

#### Wiring Diagram
<p align=center><img width="433" height="437" alt="image" src="https://github.com/user-attachments/assets/2df82816-ac34-46b1-88dd-9a2d2e15b375" />

#### Schematic
<p align=center><img width="448" height="428" alt="image" src="https://github.com/user-attachments/assets/b2a4b651-38d1-4a64-b0c2-801f958e6c78" />

## ESP 32-based IoT Sensor Node
### Workflow
* The ESP32 reads data from the DHT11 sensor.
* It publishes the readings to the Raspberry Pi (Fog Node) via MQTT.
* The Fog Node locally processes the data, sends a feedback message (e.g., “Too cold, turn on heater”), and forwards the data back to the ESP32.
* For the Cloud implementation using Adafruit IO, the data is sent to the cloud server, where data processing takes place feedback.

### Materials Used
* ESP32-WROOM-32E Dev Board
* DHT11 Sensor
* Fog Node (Raspberry Pi)
* Custom PCB for connecting DHT11 to ESP32-WROOM-32E Dev Board
* MQTT Broker

#### Custom PCB Connection Board
<p align=center /p><img width="300" height="510" alt="image" src="https://github.com/user-attachments/assets/4ed67f79-c707-4c5d-b568-2bedaba825a1" />

#### Schematic
<p align = center /p><img width="632" height="702" alt="image" src="https://github.com/user-attachments/assets/fc037a47-4225-458f-a211-8d8ac6c34095" />



## Results
Fog processing provides quicker response times since computations occur closer to the sensor, while cloud processing offers better scalability and data visibility at the cost of higher latency.

