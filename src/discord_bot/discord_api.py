from dotenv import load_dotenv
import os
import discord

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

print(discord_token)

class DiscordClient (discord.Client):
    async def on_ready ( self ):
        print(f"Logged in as {self.user}")

    async def on_message ( self , message ):
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")