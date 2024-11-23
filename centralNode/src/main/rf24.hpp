#include <SPI.h>
#include "RF24.h"

#define CE_PIN 7
#define CSN_PIN 8

#define TIMEOUTACK 2000 //us
#define TIMEOUTSEND 6000 //us

#define ACK 1

bool sendPackage(RF24* radio, char* package, uint8_t packageSize, uint8_t origin, uint8_t destination);
bool receivePackage(RF24* radio, char* package, uint8_t packageSize, uint8_t myAddress, unsigned long timeout, uint8_t* origin);
