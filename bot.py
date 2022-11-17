import constants
print('test1')
import player_search
print('test2')
import discord
from discord.ext import commands

# input: local vars
intents = discord.Intents.default()
intents.message_content = True
bot_key = constants.discord_bot_key

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot has logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('apex'):
        player_search.main()
        await message.channel.send('warmer')

client.run(bot_key)