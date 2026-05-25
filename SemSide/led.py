# Bestand: led.py (Jouw Proces 4)
import paho.mqtt.client as mqtt
from gpiozero import LED

# Pas de pinnen aan naar wat jij op je breadboard hebt!
led_groen = LED(26)
led_geel = LED(19)
led_rood = LED(13)

def on_connect(client, userdata, flags, reason_code, properties):
    print("LED Actuator verbonden met Broker!")
    client.subscribe("klimaat/ventilator/snelheid")

def on_message(client, userdata, msg):
    snelheid = msg.payload.decode('utf-8')
    print(f"Ventilator snelheid ontvangen: {snelheid}")
    
    # Reset LEDs
    led_groen.off()
    led_geel.off()
    led_rood.off()
    
    # Logica voor de lampjes op basis van Maarten's controller signalen
    if snelheid == "1":
        led_groen.on()
    elif snelheid == "2":
        led_geel.on()
    elif snelheid == "3":
        led_rood.on()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

print("LED Actuator draait. Wachten op snelheids-berichten...")
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nActuator gestopt.")
    led_groen.off(); led_geel.off(); led_rood.off()