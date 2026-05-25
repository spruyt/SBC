import paho.mqtt.client as mqtt
from gpiozero import Servo
import time

# TODO: pas deze waarden aan
MQTT_BROKER = "192.168.1.100"
MQTT_PORT = 1883
MQTT_TOPIC_VENTILATOR = "klimaat/ventilator"  # topic waarop snelheid binnenkomt
SERVO_PIN = 18  # TODO: aanpassen naar correcte GPIO pin

servo = Servo(SERVO_PIN)

def stel_snelheid_in(snelheid):
    # snelheid verwacht als getal tussen 0 en 100
    # omzetten naar servo positie: -1 (min) tot 1 (max)
    positie = (snelheid / 100.0) * 2 - 1
    servo.value = positie

def on_message(client, userdata, message):
    try:
        snelheid = float(message.payload.decode())
        snelheid = max(0, min(100, snelheid))  # begrenzen tussen 0 en 100
        print(f"Snelheid ontvangen: {snelheid}%")
        stel_snelheid_in(snelheid)
    except Exception as e:
        print(f"Fout bij verwerken bericht: {e}")

client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC_VENTILATOR)
client.loop_forever()