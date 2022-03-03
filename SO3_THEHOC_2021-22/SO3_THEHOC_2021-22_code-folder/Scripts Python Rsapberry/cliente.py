                            #!/usr/bin/env python
# -*- coding: utf8 -*-
import socket
import signal
from datetime import datetime

continue_reading = True


ClientMultiSocket = socket.socket()

host = '192.168.138.45'
port = 1234

print('Waiting for server response...')
try:
        ClientMultiSocket.connect((host, port))
except socket.error as e:
        print(str(e))

res = ClientMultiSocket.recv(1024)


str_id = "136,4,167,17"
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
    #text to voice will need to do the script

ClientMultiSocket.close()


