import os
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def initialize_db():
    print(os.getenv("FIREBASE"))

    cred_text = os.getenv("FIREBASE")
    if cred_text is not None:
        with open("fb_credential.json") as f:
            f.write(cred_text)

    uid_text = os.getenv("FIREBASE_CLIENT_ID")

    cred = credentials.Certificate('fb_credential.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://haracho-disbot-db.firebaseio.com/',
        'databaseAuthVariableOverride': {
            "uid": uid_text
        }
    })

    ref = db.reference('/bot_resource')

    member_table = ref.child('members')

    haracho_ref = member_table.child(str(713813234246746202)).child("voice_history")

    now = datetime.datetime.now()

    haracho_ref.child(str(now.timestamp()).replace(".", "d")).set({
        "time_stamp": str(now),
        "channel_id": 690909527461199922,
        "is_join": True
    })

    now = datetime.datetime.now() + datetime.timedelta(seconds=1)

    haracho_ref.child(str(now.timestamp()).replace(".", "d")).set({
        "time_stamp": str(now),
        "channel_id": 690909527461199922,
        "is_join": False
    })

    print(ref.get())

    return db
