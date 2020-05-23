"""
通話に入ってTTSするだけのクソみたいなBOT
Reference↓
https://discordpy.readthedocs.io/ja/latest/api.html
"""
import asyncio
import os
import sys

import discord
from gtts import gTTS
from mutagen.mp3 import MP3

vc_id = 683939861539192865
sound_dict = {"dai-pan": "snd/single_bullet.mp3", "bullet": "snd/multi_bullet.mp3"}

client = discord.Client()

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.content.startswith("!gtts") and not message.content.startswith("!gttse"):
        my_text = message.content.strip("!gtts ")

        language = "ja"

        output = gTTS(text=my_text, lang=language, slow=False)
        output.save("tmp/output.mp3")

        voice_client = await (client.get_channel(vc_id)).connect(reconnect=False)
        voice_client.play(discord.FFmpegPCMAudio(source="tmp/output.mp3"))
        sleep_time = MP3("tmp/output.mp3").info.length + 0.25

        await asyncio.sleep(sleep_time)
        await voice_client.disconnect(force=True)

    if message.content.startswith("!gttse"):
        my_text = message.content.strip("!gttse ")

        language = "en"

        output = gTTS(text=my_text, lang=language, slow=False)
        output.save("tmp/output.mp3")

        voice_client = await (client.get_channel(vc_id)).connect(reconnect=False)
        voice_client.play(discord.FFmpegPCMAudio(source="tmp/output.mp3"))
        sleep_time = MP3("tmp/output.mp3").info.length + 0.25

        await asyncio.sleep(sleep_time)
        await voice_client.disconnect(force=True)

    if message.content.startswith("台パン.mp3"):
        voice_client = await (client.get_channel(vc_id)).connect(reconnect=False)
        voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["dai-pan"]))
        sleep_time = MP3(sound_dict["dai-pan"]).info.length + 0.25
        await asyncio.sleep(sleep_time)
        await voice_client.disconnect(force=True)

    if message.content.startswith("!bullet"):
        voice_client = await (client.get_channel(vc_id)).connect(reconnect=False)
        voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["bullet"]))
        sleep_time = MP3(sound_dict["bullet"]).info.length + 0.25
        await asyncio.sleep(sleep_time)
        await voice_client.disconnect(force=True)

if __name__ == "__main__":
    TOKEN = os.environ["TOKEN"]
    client.run(TOKEN)
