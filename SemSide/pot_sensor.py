# Bestand: pot_sensor.py (Jouw Proces 2)
import paho.mqtt.client as mqtt
from smbus2 import SMBus
from time import sleep

# I2C instellingen
I2C_ADRES = 0x08 # Hetzelfde adres als in je Arduino code
bus = SMBus(1)   # I2C bus 1 op de Raspberry Pi

# MQTT instellingen
BROKER = "localhost" # Omdat jij zelf de broker draait
TOPIC = "klimaat/instelling/temperatuur"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, 1883, 60)

print("Temperatuur Sensor gestart. Druk op CTRL+C om te stoppen.")

try:
    while True:
        try:
            # Vraag 1 byte data aan de Arduino via I2C
            temperatuur = bus.read_byte(I2C_ADRES)
            
            # Publiceer dit naar de MQTT broker
            client.publish(TOPIC, str(temperatuur))
            print(f"Gewenste temperatuur ({temperatuur}°C) verzonden naar topic '{TOPIC}'")
            
        except OSError:
            print("Kan de Arduino niet vinden op I2C. Zitten de draadjes goed?")
            
        sleep(2) # Stuur elke 2 seconden een update (pas aan indien nodig)

except KeyboardInterrupt:
    print("\nSensor gestopt.")