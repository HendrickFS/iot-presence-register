#pragma once
#include "./main.hpp"


RF24 radio(CE_PIN, CSN_PIN);
uint64_t address[2] = { 0x3030303030LL, 0x3030303030LL};
uint8_t myAddress = 50; // Node 01: 16, Node 02: 22, Central: 50
#define TIMEOUTSEND 6000 //us

byte uid[4] = {0x00, 0x00, 0x00, 0x00};
byte package[6];

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

}

void loop() {
    radio.startListening();
    if(receivePackage(&radio, package, sizeof(package), myAddress, TIMEOUTSEND)){
        Serial.print("Package received: ");
        dumpToSerial(package, sizeof(package));
        Serial.println();
        for (byte i = 0; i < 4; i++) {
            uid[i] = package[i + 2];
        }
        Serial.print("Received: ");
        dumpToSerial(uid, sizeof(uid));
        Serial.println();
    }
    delay(10);
}

void dumpToSerial(byte* buffer, byte bufferSize) {
    for (byte i = 0; i < bufferSize; i++) {
        Serial.print(buffer[i], HEX);
    }
}
