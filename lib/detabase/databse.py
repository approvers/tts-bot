import os
import datetime
import pytz
import platform

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

JST = pytz.timezone("Asia/Tokyo")
DB_URL = "https://haracho-disbot-db.firebaseio.com/"


class DataBaseClient:
    def __init__(self, uid=None):
        self.db_entity = self.__initialize_db(uid)

        __content = "System started and data base client initialized on {}".format(platform.system())
        self.add_system_log(errtype="INFO", content=__content)

        self.cached_dict = None
        self.members_list = None
        self.fetch_cache()

    def __initialize_db(self, uid=None) -> firebase_admin.db:
        cred_text = os.getenv("FIREBASE")
        if cred_text is not None:
            with open("fb_credential.json", mode="w") as f:
                f.write(cred_text)
        cred_entity = credentials.Certificate('fb_credential.json')

        uid_text = os.getenv("FIREBASE_CLIENT_ID") if uid is None else uid

        firebase_admin.initialize_app(cred_entity, {
            'databaseURL': DB_URL,
            'databaseAuthVariableOverride': {
                "uid": uid_text
            }
        })

        return db

    def add_new_member(self, member_id: int, display_name: str):
        ref = self.db_entity.reference('/bot_resource/members')
        member_branch = ref.child(str(member_id))
        member_branch.set({
            "id": member_id,
            "display_name": display_name,
            "voice_history": {}
        })

    def add_voice_history(self, member_id: int, display_name: str, channel_id: int, is_join: bool):
        self.fetch_cache()

        now = datetime.datetime.now(JST)
        ref = db.reference('/bot_resource/members')

        # DBに記録がないユーザーの場合、新たに子を追加する
        if not str(member_id) in self.members_list:
            self.add_new_member(member_id, display_name)

        member_branch = ref.child(str(member_id))

        voice_history_branch = member_branch.child("voice_history").child(self.__time_parser(mode="stamp", time=None))
        voice_history_branch.set({
            "channel_id": channel_id,
            "is_join": is_join,
            "time_stamp": self.__time_parser(mode="str", time=now)
        })

    def add_system_log(self, errtype: str, content: str):
        syslog_ref = self.db_entity.reference("/bot_resource/system_logs")
        now = datetime.datetime.now(JST)
        branch_name = self.__time_parser(time=now, mode="stamp")
        syslog_ref.child(branch_name).set({
            "time_stamp": self.__time_parser(time=now, mode="str"),
            "type": errtype,
            "content": content
        })

    def fetch_cache(self):
        self.cached_dict = self.db_entity.reference("/bot_resource")
        self.members_list = (self.db_entity.reference("/bot_resource").child("members").get()).keys()

    # TODO: （↓インスタンスメソッドである必要性が）ないです。
    def __time_parser(self, mode, time=None):
        if type(time) is not datetime.datetime and time is not None:
            err_msg = "Excepted datetime.datetime object but got {}".format(type(time))
            raise(TypeError(err_msg))
        else:
            time = datetime.datetime.now(JST)

        if mode in ["str", "string"]:
            return str(time)

        if mode == "stamp":
            return (str(time.timestamp())).replace(".", "d")
