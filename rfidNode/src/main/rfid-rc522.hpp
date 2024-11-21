#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

struct CacheUid {
    byte uid[4];
    unsigned long timeout;
};

bool readRFID(byte* uid, MFRC522 rfid);

void initializeCache(CacheUid* cache, byte cacheSize);
bool isInCache(byte* uid, CacheUid* cache, byte cacheSize);
void addToCache(byte* uid, CacheUid* cache, byte cacheSize, unsigned long timeout);
void removeFromCache(byte* uid, CacheUid* cache, byte cacheSize);
void updateCache(CacheUid* cache, byte cacheSize);