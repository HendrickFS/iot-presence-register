#include "rf24.hpp"

bool sendPackage(RF24* radio, char* package, uint8_t packageSize, uint8_t origin, uint8_t destination) {
    package[0]=destination;
    package[1]=origin;
    char packageACK[3];
    bool sent = false;
    unsigned long start_timer = micros();                // start the timer
    while(micros()-start_timer<TIMEOUTSEND){ // Try to send the package for the timeout defined
        radio->startListening();
        delayMicroseconds(70);
        radio->stopListening();
        if (!radio->testCarrier()) {
            radio->write(&package[0], packageSize);
            sent=true;
            // Serial.println("S"); // Success sending
            break;
        }else{
            // Serial.println("W"); // Waiting for channel to be available
            delayMicroseconds(150);
        }
    }
    if(!sent){
        return false; // Failed to send: stop here
    }
    // Success sending, now wait for ACK
    unsigned long start_timer_ack = micros();
    radio->startListening();
    while(micros()-start_timer_ack<TIMEOUTACK){ // Try to receive the ACK for the timeout defined
        if (radio->available()) { 
        radio->read(&packageACK[0],3);
        if(packageACK[0]==origin && packageACK[1]==destination && packageACK[2] == ACK){
            unsigned long end_timer = micros();                  // end the timer
            Serial.print(end_timer - start_timer);  // print the timer result
            return true;
        }
        radio->flush_rx(); // Flush the buffer
        }
    }
    return false;
}

bool receivePackage(RF24* radio, char* package, uint8_t packageSize, uint8_t myAddress, unsigned long timeout, uint8_t* origin) {
    char packageACK[3];
    unsigned long start_timer = micros();                // start the timer
    bool sent = false;
    bool received = false;
    radio->startListening();
    while(micros()-start_timer<timeout){ // Try to receive the package for the timeout defined
        if (radio->available()) {
            radio->read(&package[0], packageSize);
            if(package[0]==myAddress){
                *origin=package[1];
                received=true;
                // Serial.println("R"); // Success receiving
                break;
            }
            radio->flush_rx(); // Flush the buffer
        }
    }
    radio->flush_rx(); // Flush the buffer
    if(!received){
        return false; // Failed to receive: stop here
    }


    // Success receiving, now send ACK
    packageACK[0]=package[1];
    packageACK[1]=package[0];
    packageACK[2]=ACK;
    start_timer = micros();                // start the timer
    while(micros()-start_timer<TIMEOUTACK){ // Try to send the ACK for the timeout defined
        radio->startListening();
        delayMicroseconds(70);
        radio->stopListening();
        if (!radio->testCarrier()) {
            radio->write(&packageACK[0], 3);
            sent=true;
            // Serial.println("S"); // Success sending
            break;
        }else{
            // Serial.println("W"); // Waiting for channel to be available
            delayMicroseconds(150);
        }
    }

    if(!sent){
        return false; // Failed to send: stop here
    }

    return true;
}