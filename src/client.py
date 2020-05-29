"""
通話に入ってTTSするだけのクソみたいなBOT
Reference↓
https://discordpy.readthedocs.io/ja/latest/api.html
"""
import asyncio
import os
import time

import discord
from gtts import gTTS
from mutagen.mp3 import MP3

from src.message.root import MessageRoot

vc_id = 683939861539192865
sound_dict = {"dai-pan": "ast/snd/single_bullet.mp3",
              "bullet": "ast/snd/multi_bullet.mp3",
              "scream": "ast/snd/screaming-beaber.mp3",
              "urusai": "ast/snd/shut-up.mp3",
              "AC": "ast/snd/AC_Buzzer.mp3",
              "WA": "ast/snd/WA_Buzzzer.mp3",
              "chino": "ast/snd/first.wav"}


class MainClient(discord.Client):
    def __init__(self):
        super().__init__()

    def run(self):
        super().run(os.environ["TOKEN"])

    async def on_ready(self):
        self.message_manager = MessageRoot(self)

    async def on_message(self, message):
        if r"https://www.dlsite.com/maniax/work/=/product_id/RJ224037.html/" in message.content:
            await message.delete(delay=None)

        if message.content.startswith("!announce") and not message.content.startswith("!announcee"):
            my_text = message.content.strip("!announce ")

            language = "ja"

            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source="snd/pppp.mp3"))

            ut = time.time()
            output = gTTS(text=my_text, lang=language, slow=False)
            output.save("tmp/output.mp3")
            await asyncio.sleep(0 if (5 - (time.time() - ut)) < 0 else (5 - (time.time() - ut)))
            voice_client.stop()

            voice_client.play(discord.FFmpegPCMAudio(source="tmp/output.mp3"))
            sleep_time = MP3("tmp/output.mp3").info.length + 0.25

            await asyncio.sleep(sleep_time)
            voice_client.stop()

            voice_client.play(discord.FFmpegPCMAudio(source="snd/pppp_end.mp3"))
            await asyncio.sleep(5)

            await voice_client.disconnect(force=True)

        if message.content.startswith("!announcee"):
            my_text = message.content.strip("!announcee ")

            language = "en"

            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source="snd/pppp.mp3"))

            ut = time.time()
            output = gTTS(text=my_text, lang=language, slow=False)
            output.save("tmp/output.mp3")
            await asyncio.sleep(0 if (5 - (time.time() - ut)) < 0 else (5 - (time.time() - ut)))
            voice_client.stop()

            voice_client.play(discord.FFmpegPCMAudio(source="tmp/output.mp3"))
            sleep_time = MP3("tmp/output.mp3").info.length + 0.25

            await asyncio.sleep(sleep_time)
            voice_client.stop()

            voice_client.play(discord.FFmpegPCMAudio(source="snd/pppp_end.mp3"))
            await asyncio.sleep(5)

            await voice_client.disconnect(force=True)

        if message.content.startswith("!gtts") and not message.content.startswith("!gttse"):
            my_text = message.content.strip("!gtts ")

            language = "ja"

            output = gTTS(text=my_text, lang=language, slow=False)
            output.save("tmp/output.mp3")

            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source="tmp/output.mp3"))
            sleep_time = MP3("tmp/output.mp3").info.length + 0.25

            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("!gttse"):
            my_text = message.content.strip("!gttse ")

            language = "en"

            output = gTTS(text=my_text, lang=language, slow=False)
            output.save("tmp/output.mp3")

            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source="tmp/output.mp3"))
            sleep_time = MP3("tmp/output.mp3").info.length + 0.25

            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("台パン.mp3"):
            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["dai-pan"]))
            sleep_time = MP3(sound_dict["dai-pan"]).info.length + 0.25
            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("!bullet"):
            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["bullet"]))
            sleep_time = MP3(sound_dict["bullet"]).info.length + 0.25
            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("!scream"):
            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["scream"]))
            sleep_time = MP3(sound_dict["scream"]).info.length + 0.25
            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("!urusai") or message.content.startswith("!shut-up"):
            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["urusai"]))
            sleep_time = MP3(sound_dict["urusai"]).info.length - 0.25
            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("!ac") or message.content.startswith("!right"):
            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["AC"]))
            sleep_time = MP3(sound_dict["AC"]).info.length - 0.25
            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("!wa") or message.content.startswith("!wrong"):
            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["WA"]))
            sleep_time = MP3(sound_dict["WA"]).info.length - 0.25
            await asyncio.sleep(sleep_time)
            await voice_client.disconnect(force=True)

        if message.content.startswith("!chino"):
            voice_client = await (self.get_channel(vc_id)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source=sound_dict["chino"]))
