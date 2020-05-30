import datetime
import pytz

import firebase_admin
from firebase_admin import db

from src.databse.initialize import initialize_db
from src.databse.structures import new_member
from src.databse.structures import new_voice_history

db = initialize_db()
JST = pytz.timezone("Asia/Tokyo")


def add_on_voice(member_id: int, display_name: str, channel_id: int, is_join: bool):
    print("change detected", member_id, display_name, channel_id, is_join)
    now = datetime.datetime.now(JST)
    parsed_timestamp = str(now.timestamp()).replace(".", "d")
    ref = db.reference('/bot_resource/members')
    members_dict = ref.get()

    # DBに記録がないユーザーの場合、新たに子を追加する
    if not str(member_id) in members_dict.keys():
        member_branch = ref.child(str(member_id))
        member_branch.set(new_member(member_id, display_name))

    member_branch = ref.child(str(member_id))

    voice_history_branch = member_branch.child("voice_history").child(parsed_timestamp)
    voice_history_branch.set(new_voice_history(now, channel_id, is_join))
