import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received message on topic", message.topic)
    print("Message payload", message.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect("<input broker host>", "<input broker port>")

client.subscribe([("heart_rate", 0), ("blood_pressure", 0)])
client.loop_forever()

