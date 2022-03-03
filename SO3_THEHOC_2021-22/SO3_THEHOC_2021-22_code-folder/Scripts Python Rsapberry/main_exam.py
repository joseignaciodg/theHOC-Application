#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import mfrc522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = mfrc522.MFRC522()

# Welcome message
print ("MFRC522 data read")
print ("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("RFID Sticker detected ")

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print ("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

        if uid[0] == 136 and uid[1] == 4 and uid[2] == 7 and uid[3] == 52:
            exec(open("weather.py").read())
            exec(open("texttovoice_weather.py").read())

        elif uid[0] == 136 and uid[1] == 4 and uid[2] == 195 and uid[3] == 17:
            exec(open("time.py").read())
            exec(open("texttovoice_hora.py").read())


        elif uid[0] == 136 and uid[1] == 4 and uid[2] == 167 and uid[3] == 17:
            exec(open("make_call_twilio.py").read())

        elif uid[0] == 136 and uid[1] == 4 and uid[2] == 2 and uid[3] == 52:
            exec(open("alarm.py").read())
