import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate('secret_key.json')


firebase_admin.initialize_app (cred, {
    'databaseURL' : "https://hoc21-3f4e6-default-rtdb.europe-west1.firebasedatabase.app"
})

ref = db.reference('location')

print (ref.get())
print ('Ok!')

