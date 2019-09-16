import paho.mqtt.publish as mqtt

# Name of broker: Mosquitto
# Server Name
server_name = "localhost"
# Port Number
port_num = 1883

# Topic to publish to
topic = "home/temperature"
# Message to send
message = "75 F"

mqtt.single(topic, message, hostname=server_name)