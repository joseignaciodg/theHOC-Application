                            #!/usr/bin/env python
# -*- coding: utf8 -*-
import socket
import signal
from datetime import datetime

import RPi.GPIO as GPIO
import mfrc522
import signal

continue_reading = True

ClientMultiSocket = socket.socket()

host = '192.168.138.45'
port = 1234

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

print('Waiting for server response...')
try:
        ClientMultiSocket.connect((host, port))
except socket.error as e:
        print(str(e))

res = ClientMultiSocket.recv(1024)

signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = mfrc522.MFRC522()

    # Scan for cards
(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
if status == MIFAREReader.MI_OK:
    print ("RFID Sticker detected ")

(status,uid) = MIFAREReader.MFRC522_Anticoll()

# Welcome message
print ("MFRC522 data read")
print ("Press Ctrl-C to stop.")

str_id = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

ClientMultiSocket.send(str_id.encode('utf-8'))
action = ClientMultiSocket.recv(1024)

if action == '0':
    print ('Phone Calls')
elif action == '1':
    print ('Play Music')
    exec(open("music.py").read())
elif action == '2':
    print ('Weather Info')
    exec(open("weather.py").read())
    exec(open("texttovoice_weather.py").read())
elif action == '4':
    print ('Alarm Clock')
    exec(open("alarm.py").read())
elif action == '5':
    print ('Current Time')
    exec(open("weather.py").read())
    exec(open("texttovoice_weather.py").read())
else:
    print (action)
    action[2:]
    text_file = open("tasks.txt", "w")
    n = text_file.write(action[2:])
    text_file.close()
    exec(open("texttovoice_tasks.py").read())#text to voice will need to do the script

ClientMultiSocket.close()
