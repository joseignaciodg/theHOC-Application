import socket
import os
from _thread import *
import random
import time

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from datetime import datetime

cred = credentials.Certificate("secret_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def getDataDB_Functionalities(data):

	db = firestore.client()

	sticker = data
	action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')

	return action
	
	
def calendar():

        day = str(datetime.now().day)
        if len(day)==1:
            day = '0'+str(day)

        month = str(datetime.now().month)
        if len(month)==1:
            month = '0'+str(month)

        today = str(datetime.now().year)+'/'+month+'/'+day
       
        docs = db.collection(u'task').stream()
        for doc in docs:
            if(doc.to_dict().get('dateTime').split()[0] == today):
                everything = doc.to_dict().get('name')
                #print(doc.to_dict().get('name')+' => dateTime: '+doc.to_dict().get('dateTime'))
                return everything	

ServerSideSocket = socket.socket()

host = '192.168.138.45' 
port = 1234		  

CounterConnections = 0
try:
	ServerSideSocket.bind((host, port))
except socket.error as e:
	print(str(e))

print('Server is listening on IP '+ host)
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server connected'))

    data = connection.recv(2048)
    info = getDataDB_Functionalities(data.decode('utf-8'))
    print (info)

    info = str(info)

    if (info != '3' and info != '0'):
        connection.sendall(info.encode('utf-8'))
    elif info == '3': # calendar events
        ev = calendar()
        print (ev)
        if ev == None:
            info = "There is not tasks for today"
        else:
            info = ev
        connection.sendall(info.encode('utf-8'))
    elif info == '0': #phone call 
        connection.send(info.encode('utf-8')) 
        db.collection(u'meet').document(u'0').update({u'ramdom': random.random()})
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    CounterConnections += 1
    print('Connection Number: ' + str(CounterConnections))

ServerSideSocket.close()
