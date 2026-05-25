import smbus2
import struct
import paho.mqtt.client as mqtt
import time

I2C_BUS = 1
I2C_ADRES = 0x08
MQTT_BROKER = "192.168.1.100"  # aanpassen
MQTT_PORT = 1883
MQTT_TOPIC = "groep1/klimaat/temperatuur"  # aanpassen

bus = smbus2.SMBus(I2C_BUS)
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

def lees_temperatuur():
    data = bus.read_i2c_block_data(I2C_ADRES, 0, 4)
    temperatuur = struct.unpack('f', bytes(data))[0]
    return round(temperatuur, 2)

while True:
    try:
        temperatuur = lees_temperatuur()
        print(f"Temperatuur: {temperatuur} °C")
        client.publish(MQTT_TOPIC, str(temperatuur))
    except Exception as e:
        print(f"Fout: {e}")
    time.sleep(1)