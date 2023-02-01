from src.chatgpt_ai.openai import create_chatgpt_response
import discord

commands = ['/ai', '/bot']

class DiscordClient (discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        command, user_message = None, None
        print(f"Message from {message.author}: {message.content}")
        for text in commands:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(f"command: {command}, user_message: {user_message}")
        
        if command in commands:
            bot_response = create_chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")

intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)
