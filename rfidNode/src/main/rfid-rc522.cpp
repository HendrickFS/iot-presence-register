#include "./rfid-rc522.hpp"

bool compareUid(byte* uid1, byte* uid2) {
    for (byte i = 0; i < 4; i++) {
        if (uid1[i] != uid2[i]) {
            return false;
        }
    }
    return true;
}


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



void initializeCache(CacheUid* cache, byte cacheSize) {
    for (byte i = 0; i < cacheSize; i++) {
        for(byte j = 0; j < 4; j++) {
            cache[i].uid[j] = 0;
        }
        cache[i].timeout = 0;
    }
}

bool isInCache(byte* uid, CacheUid* cache, byte cacheSize) {
    for (byte i = 0; i < cacheSize; i++) {
        if (compareUid(uid, cache[i].uid)) {
            return true;
        }
    }
    return false;
}

void addToCache(byte* uid, CacheUid* cache, byte cacheSize, unsigned long timeout) {
    for (byte i = 0; i < cacheSize; i++) {
        if (cache[i].timeout == 0) {
            for(byte j = 0; j < 4; j++) {
                cache[i].uid[j] = uid[j];
            }
            cache[i].timeout = timeout;
            return;
        }
    }
}

void removeFromCache(byte* uid, CacheUid* cache, byte cacheSize) {
    for (byte i = 0; i < cacheSize; i++) {
        if (compareUid(uid, cache[i].uid)) {
            for(byte j = 0; j < 4; j++) {
                cache[i].uid[j] = 0;
            }
            cache[i].timeout = 0;
            return;
        }
    }
}

void updateCache(CacheUid* cache, byte cacheSize) {
    for (byte i = 0; i < cacheSize; i++) {
        if (cache[i].timeout > 0) {
            cache[i].timeout--;
        } else{
            for(byte j = 0; j < 4; j++) {
                cache[i].uid[j] = 0;
            }
        }
    }
}