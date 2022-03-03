import firebase_admin
import random
from firebase_admin import firestore
from firebase_admin import credentials
from datetime import datetime

def actions(action, button):
    start = datetime.now()
    time_action = 0
    if action == 0:
        while(not button and time_action<1):
            #if button is pressed:
                #button = True 
            end = datetime.now()
            time_action = end.second - start.second
        db.collection(u'meet').document(u'0').update({u'ramdom': random.random()})
        print("Phone Calls")

    elif action == 1:
        while(not button and time_action<1):
            #if button is pressed:
                #button = True 
            end = datetime.now()
            time_action = end.second - start.second
        
        print("Play Music")

    elif action == 2:
        while(not button and time_action<1):
            #if button is pressed:
                #button = True 
            end = datetime.now()
            time_action = end.second - start.second
        latitude = db.collection(u'location').document(u'0').get().to_dict().get('latitude')
        longitude = db.collection(u'location').document(u'0').get().to_dict().get('longitude')
        print("Weather information")
        print(" -> Latitude: "+str(latitude))
        print(" -> Longitude: "+str(longitude))

    elif action == 3:
        while(not button and time_action<1):
            #if button is pressed:
                #button = True 
            end = datetime.now()
            time_action = end.second - start.second
        
        print("Calendar Events")

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
                print(doc.to_dict().get('name')+' => dateTime: '+doc.to_dict().get('dateTime'))
                

    elif action == 4:
        while(not button and time_action<1):
            #if button is pressed:
                #button = True 
            end = datetime.now()
            time_action = end.second - start.second
        
        print("Alarm Clock")

    elif action == 5:
        while(not button and time_action<1):
            #if button is pressed:
                #button = True 
            end = datetime.now()
            time_action = end.second - start.second
        
        print("Current Time")
        print(str(datetime.now().hour)+"h "+str(datetime.now().minute)+"min")



if  __name__ ==  '__main__':
    cred = credentials.Certificate("hoc21-3f4e6-firebase-adminsdk-5la5l-5f981d1257.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    sticker = '' #se escanea el sticker y se almacena su valor
    confirm_button = False

    if sticker == '136,4,11,52':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,167,17':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,171,17':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,175,17':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,178,16':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,182,16':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,195,17':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,2,52':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,213,17':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

    elif sticker == '136,4,7,52':
        action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')
        actions(action, confirm_button)

