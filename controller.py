# Author: Gerardo Sanchez
# Date created: June 2, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Controller Publisher")
publisher_client.connect(broker_address)

def on_messages(client,userdata,message):
    if message.topic == "Tanks/heights/h1":
        controller.h1 = float(message.payload.decode("utf-8"))
    if message.topic == "Tanks/heights/h2":
        controller.h2 = float(message.payload.decode("utf-8"))
    if message.topic == "Tanks/heights/h3":
        controller.h3 = float(message.payload.decode("utf-8"))
    if message.topic == "Tanks/constants/a":
        controller.a = float(message.payload.decode("utf-8"))
    if message.topic == "Tanks/constants/A":
        controller.A = float(message.payload.decode("utf-8"))

listener_client = mqtt.Client("Controller Listener")
listener_client.on_message = on_messages
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tanks/#")


# Controller
def controller():
    controller.q = 0.1*controller.h1 + 0.1*controller.h2 + 0.1*controller.h3
    publisher_client.publish("Tanks/flows/q", controller.q)
    #print("MQTT is sending flow q: " + str(controller.q))

# Controller parameters
controller.h1 = 0
controller.h2 = 0
controller.h3 = 0
controller.q = 0
controller.a = 0.00013104
controller.A = 0.03

while True:
    controller()
    time.sleep(0.05)
