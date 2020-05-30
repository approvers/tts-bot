import json

import discord

with open("sndconfig.json", mode="r") as f:
    sounds = json.load(f)

non_commands = {"台パン.mp3": "ast/snd/single_bullet.mp3",
                "announce-start": "ast/snd/pppp.mp3",
                "announce-end": "ast/snd/pppp_end.mp3"}


def message_root(message: discord.Message):
    pass
