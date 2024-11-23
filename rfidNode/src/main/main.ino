#pragma once
#include "./main.hpp"

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
// 
MFRC522::MIFARE_Key key;

// Create a cache of 10 elements to store a timeout until the card is valid again
CacheUid cache[10];
byte cacheSize = 10;
byte uid[4];
bool enabled = true;
byte package[6];

RF24 radio(CE_PIN, CSN_PIN);
uint64_t address[2] = { 0x3030303030LL, 0x3030303030LL};
uint8_t myAddress = 22; // Node 01: 16, Node 02: 22, Central: 50
uint8_t destination = 50;
uint8_t origin;

void setup() {
    Serial.begin(9600); // Initialize serial communications with the PC
    while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)

    // Setup the radio
    if(!radio.begin()){
        Serial.println("radio begin failed");
        while(1);
    }
    radio.setPALevel(RF24_PA_MAX);
    radio.setAutoAck(false);
    radio.disableCRC();
    radio.setDataRate(RF24_1MBPS);
    radio.setPayloadSize(sizeof(package));
    radio.openWritingPipe(address[0]);
    radio.openReadingPipe(1,address[1]);
    radio.setChannel(100); // REMEMBER TO CHANGE THIS ON LOOP TO FIND A GOOGD CHANNEL
    radio.startListening();
    radio.stopListening();
    radio.flush_rx();

    // Setup the RFID
    SPI.begin();        // Init SPI bus
    mfrc522.PCD_Init(); // Init MFRC522 card

    for (byte i = 0; i < 6; i++) {
        key.keyByte[i] = 0xFF;
    }

    Serial.println(F("Ready to read RFID card"));

    initializeCache(cache, cacheSize);
}

void loop() {
  updateCache(cache, cacheSize);

  if (readRFID(uid, mfrc522) && enabled) {
    if (isInCache(uid, cache, cacheSize)) {
      return;
    } else {
      addToCache(uid, cache, cacheSize, 1000);
      dumpToSerial(uid, 4);
      Serial.println();
    }

    package[0] = destination;
    package[1] = myAddress;
    for (byte i = 0; i < 4; i++) {
      package[i + 2] = uid[i];
    }

    Serial.print("Package sent: ");
    dumpToSerial(package, sizeof(package));
    Serial.println();

    if (sendPackage(&radio, package, sizeof(package), myAddress, destination)) {
      Serial.println("Sent");
    } else {
      Serial.println("Failed to send");
    }
  }
  radio.startListening();
  if(receivePackage(&radio, package, sizeof(package), myAddress, TIMEOUTSEND, &origin)){
      Serial.print("Package received: ");
      dumpToSerial(package, sizeof(package));
      Serial.println();
      if (verifySignal(package, sizeof(package))) {
          Serial.println("Signal received");
          enabled = !enabled;
      }
  }   
  Serial.flush();
}

void dumpToSerial(byte* buffer, byte bufferSize) {
    for (byte i = 0; i < bufferSize; i++) {
        Serial.print(buffer[i], HEX);
    }
}

bool verifySignal(byte* package, byte packageSize) {
    for(byte i = 2; i < packageSize; i++) {
        if(package[i] != 0x00) {
            return false;
        }
    }
    return true;
}