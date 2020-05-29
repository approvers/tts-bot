import discord


class MessageRoot:
    def __init__(self):
        pass

    async def analysis_message(self, message: discord.Message):
        pass


class CommandRoot:
    PREFIX = "!"
    PREFIX_LENGTH = len(PREFIX)

    def __init__(self, client: discord.Client):
        pass
