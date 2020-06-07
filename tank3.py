# Authors: Fatma Nur Arabaci & Gerardo Sánchez
# Date created: May 30, 2020

import paho.mqtt.client as mqtt
import time
import socket

################ WEBSOCKET receiver
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost',7777))

################ WEBSOCKET sender
broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 3 Publisher")
publisher_client.connect(broker_address)

'''
def h2_received(client,userdata,message):
    tank3.h2 = float(message.payload.decode("utf-8"))
    print("received Tank 2 h2: " + str(tank3.h2))

listener_client = mqtt.Client("Tank 3 listener")
listener_client.on_message = h2_received
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tanks/heights/h2")
'''

# Tank dynamics
def tank3():
    ################ WEBSOCKET receiver
    data, addr = sock.recvfrom(1024)
    print ("received  websocket message: ", data.decode())
    tank3.h2 = float(data)#.decode()

    tank3.h3 = tank3.h2 + 0.01
    publisher_client.publish("Tanks/heights/h3",tank3.h3)
    print("MQTT is sending Tank 3 h3: " + str(tank3.h3))

# Tank parameters
tank3.h2 = 0
tank3.h3 = 0

while True:
    tank3()
    time.sleep(0.05)
