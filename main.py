import discord
import logging
import configparser
from discord.ext import commands
import json

# Set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

print(f"discord.py version: {discord.__version__}")

# Loading config
config = configparser.ConfigParser()
config.read('config.ini')

# Set up bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config["Bot"]["Prefix"], intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

    # Get list of cogs and load them
    for cog in json.loads(config["Bot"]["Cogs"]):
        try:
            await bot.load_extension(cog)
            print(f"Successfully loaded {cog}")
        except Exception as e:
            print(f"Failed to load {cog}: {e}")

if __name__ == '__main__':
    bot.run(token=config["Discord"]["Token"])
