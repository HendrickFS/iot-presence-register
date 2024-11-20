#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

bool readRFID(byte* uid, MFRC522 rfid);