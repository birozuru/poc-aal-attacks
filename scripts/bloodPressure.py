import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import random
import time

# Declare the Broker Host Variables
broker_address = ""
broker_port    = ""
topic          = "blood_pressure"

def simulate_blood_pressure():
    systolic  = random.randint(90, 140)
    diastolic = random.randint(60,90)

    return systolic, diastolic

def on_publish(client, userdata, result):
    print("data published \n")
    pass

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client            = mqtt.Client(paho.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

client.connect(broker_address, broker_port)

while True:
    systolic, diastolic = simulate_blood_pressure()

    client.publish(topic, f"{systolic}/{diastolic}")
    print("Published blood pressure:", f"{systolic}/{diastolic}")

    time.sleep(random.uniform(1,5))