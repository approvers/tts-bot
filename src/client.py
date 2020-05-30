"""
† ダガー †
"""
import os
import asyncio

import discord

from src.on_message.root import message_root
import src.databse.root

class MainClient(discord.Client):
    def __init__(self):
        super().__init__()

    def run(self):
        super().run(os.environ["TOKEN"])

    async def on_ready(self):
        pass

    async def on_message(self, message):
        if message.author.bot:
            return
        commands = [
            "台パン.mp3",
            "!bullet",
            "!scream",
            "!ac",
            "!wa",
            "!gtts"
            "!announce"
        ]
        if message.content.strip(" ") in commands:
            await message.channel.send(("<@!{}>、firebase対応に従って大規模リファクタ中です！" +
                                        "\nすぐにまた使えるようになるので待っててね" +
                                        "\nただし`!urusai`は回復ポイントなので残っています").format(message.author.id))

        if message.content.startswith("!urusai") or message.content.startswith("!shut-up"):
            voice_client = await (self.get_channel(683939861539192865)).connect(reconnect=False)
            voice_client.play(discord.FFmpegPCMAudio(source="ast/snd/shut-up.mp3"))
            await asyncio.sleep(3)
            await voice_client.disconnect(force=True)


    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        if before.channel is None:
            src.databse.root.add_on_voice(member.id, member.display_name, after.channel.id, is_join=True)
            return
        if after.channel is None:
            src.databse.root.add_on_voice(member.id, member.display_name, before.channel.id, is_join=False)
            return
