from src.discord_bot.discord_api import client
from src import DISCORD_TOKEN

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
