#include "./main.hpp"

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
// 
MFRC522::MIFARE_Key key;


void setup() {
    Serial.begin(9600); // Initialize serial communications with the PC
    while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
    SPI.begin();        // Init SPI bus
    mfrc522.PCD_Init(); // Init MFRC522 card

    for (byte i = 0; i < 6; i++) {
        key.keyByte[i] = 0xFF;
    }

    Serial.println(F("Ready to read RFID card"));

}

void loop() {
  byte uid[4];
  if (readRFID(uid, mfrc522)) {
    Serial.print(F("UID: "));
    dumpToSerial(uid, 4);
    Serial.println();
  }

}

void dumpToSerial(byte* buffer, byte bufferSize) {
    for (byte i = 0; i < bufferSize; i++) {
        Serial.print(buffer[i], HEX);
    }
}
