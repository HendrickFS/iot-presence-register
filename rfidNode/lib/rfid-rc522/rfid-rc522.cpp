#include "./rfid-rc522.hpp"

bool readRFID(byte* uid, MFRC522 mfrc522) {
    for (byte i = 0; i < 4; i++) {
      uid[i] = 0;
    }
    if ( ! mfrc522.PICC_IsNewCardPresent())
          // Serial.println("no card");
          return false;

      // Select one of the cards
      if ( ! mfrc522.PICC_ReadCardSerial())
          // Serial.println("select");
          return false;

      for (byte i = 0; i < mfrc522.uid.size; i++) {
        uid[i] = mfrc522.uid.uidByte[i];
      }
      return true;
}