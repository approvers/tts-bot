"""
† ダガー †
"""
import os

import discord

from src.on_message.root import MessageRoot
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

    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        if before.channel is None:
            src.databse.root.add_on_voice(member.id, member.display_name, after.channel.id, is_join=True)
            return
        if after.channel is None:
            src.databse.root.add_on_voice(member.id, member.display_name, before.channel.id, is_join=False)
            return
