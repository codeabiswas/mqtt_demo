import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):

    # The topic to subscribe to
    topic = "home/temperature"

    # Subscribe to the topic after connection has been establishedw
    client.subscribe(topic)

def on_message(client, userdata, message):
    print("Message: ", str(message.payload.decode("utf-8")))
    print("Topic: ", message.topic)
    print("QOS: ", message.qos)
    print("Retain Flag: ", message.retain)

# Server Name
server_name = "localhost"
# Port Number
port_num = 1883

# Create a client instance
client = mqtt.Client()

# Callback functions on certain actions are attached here
client.on_connect = on_connect
client.on_message = on_message

# Connect the client to the broker and the appropriate port number
client.connect(server_name, port=port_num)

# Loop this client forever
client.loop_forever()