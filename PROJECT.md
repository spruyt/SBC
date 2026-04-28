Project: IoT Climate Control
Concept
Een volledig modulair IoT-systeem dat een accumulatieverwarming regelt. De kern: meting → controller → actuator, allemaal via MQTT.

Componenten (elk een apart proces)
1. Temperatuursensor (RPi #1) -- Maarten

Arduino leest een NTC via zijn ADC
RPi #1 ontvangt die waarde via I²C
RPi #1 publiceert dit als MQTT-bericht

2. Temperatuurinstelling (RPi #2) -- Sem

Arduino leest een potentiometer via zijn ADC
RPi #2 ontvangt die waarde via I²C
RPi #2 publiceert dit als MQTT-bericht

3. Actuator: ventilator (ook op RPi #1) -- Maarten

Ontvangt MQTT-berichten
Stuurt een servo aan via PWM (hoek = snelheid)
Volledig onafhankelijk van de sensorcode op RPi #1 → 2 aparte processen

4. Actuator: LED-indicatie (ook op RPi #2) -- Sem

Ontvangt MQTT-berichten
3 LED's (groen/geel/rood) geven aan of de ventilator draait en hoe snel
Opnieuw volledig onafhankelijk van de potentiometercode op RPi #2 → 2 aparte processen

5. IoT Controller (op één RPi, niet dezelfde als de MQTT broker) --> Maarten

Ontvangt alle MQTT-berichten
Logica: als gevraagde temp (pot) > gemeten temp (NTC) → ventilator aan
Hoe groter het verschil, hoe sneller de ventilator draait
Stuurt de nodige MQTT-berichten naar de actuatoren

6. MQTT Broker --> Sem

Private broker, zelf te installeren op één van de RPi's
Op een andere RPi dan de controller (load verdelen)


Hardwareopstelling samengevat
ComponentDraait opNTC sensor + I²C → MQTTRPi #1Ventilator (servo) actuatorRPi #1 (apart proces)Potentiometer + I²C → MQTTRPi #2LED-indicatie actuatorRPi #2 (apart proces)IoT ControllerRPi #1 of #2MQTT BrokerDe andere RPi

In te dienen

Logboek (wie deed wat, technische info, problemen) → PDF
Alle code als losse bestanden met correcte extensie
Foto's van de hardwareopstellingen
Video (MP4, 1080p) met demo — beide teamleden moeten aan het woord komen

Deadline
Zondag 31 mei, 23:59