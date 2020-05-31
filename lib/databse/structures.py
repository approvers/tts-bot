import datetime


def new_member(member_id: int, display_name: str):
    member_structure = {
        "id": member_id,
        "display_name": display_name,
        "voice_history": {},
        "system_log": {}
    }
    return member_structure


def new_voice_history(time: datetime.datetime, channel_id: int, is_join: bool):
    voice_history_structure = {
        "time_stamp": str(time),
        "channel_id": channel_id,
        "is_join": is_join
    }
    return voice_history_structure
