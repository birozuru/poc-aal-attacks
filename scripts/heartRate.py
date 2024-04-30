import paho.mqtt.publish as publish
import paho.mqtt.client as paho
import random
import time

# Declare the Broker Host Variables
broker_address = ""
broker_port    = ""
topic          = "heart_rate"

# Define the heart rate simulation method
def simulate_heart_rate():
    return random.randint(60, 100)

# Define mqtt publish method
def on_publish(client, userdata, result):
    print("data published \n")
    pass

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = paho.Client(paho.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

client.connect(broker_address, broker_port)

while True:
    heart_rate = simulate_heart_rate()

    client.publish(topic, str(heart_rate))
    print("Published heart rate:", heart_rate)

    time.sleep(random.uniform(1,5))