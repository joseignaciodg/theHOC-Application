import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("secret_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
sticker = '136,4,167,17'

action = db.collection(u'sticker').document(sticker).get().to_dict().get('action')

print (action)
