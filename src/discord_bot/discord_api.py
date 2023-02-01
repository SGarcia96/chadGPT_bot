from dotenv import load_dotenv
from src.chatgpt_ai import create_chatgpt_response
import os
import discord

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

commands = ['/ai', '/bot']

class DiscordClient (discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        command, user_message = None, None

        check_commands_in_message(message)

        if command in commands:
            bot_response = create_chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")

intents = discord.Intents.default()
intents.message.content = True

client = DiscordClient(intents=intents)


# Functions
def check_commands_in_message(message):
    for text in commands:
        if message.content.startswitch(text):
            command = message.content.split(' ')[0]
            user_message = message.content.replace(text, '')
            print(command, user_message)
