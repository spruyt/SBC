#include <Wire.h>

const int potPin = A0;
byte gewensteTemperatuur = 0;

void setup() {
  // Start I2C als "Slave" met adres 0x08
  Wire.begin(8);                
  
  // Vertel de Arduino welke functie hij moet draaien als de Pi om data vraagt
  Wire.onRequest(requestEvent); 
  
  // Start de seriële monitor
  Serial.begin(9600);
  Serial.println("Arduino I2C Sensor gestart! Wachten op draaiknop...");
}

void loop() {
  // Lees de knop (waarde tussen 0 en 1023)
  int potWaarde = analogRead(potPin);
  
  // Reken dit om naar een temperatuur (bijv. 15 tot 30 graden)
  gewensteTemperatuur = map(potWaarde, 0, 1023, 0, 30);
  
  // Print de waardes naar de Seriële Monitor voor debugging
  Serial.print("Ruwe knopwaarde: ");
  Serial.print(potWaarde);
  Serial.print("  --->  Berekende Temp: ");
  Serial.print(gewensteTemperatuur);
  Serial.println(" °C");
  
  delay(500); // Wacht een halve seconde zodat de monitor rustig leesbaar blijft
}

// Deze functie wordt op de achtergrond getriggerd zodra de Raspberry Pi om data vraagt
void requestEvent() {
  Wire.write(gewensteTemperatuur); // Stuur de berekende temperatuur over I2C
}