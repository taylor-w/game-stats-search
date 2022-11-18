# imports
import constants
import player_search
import discord
import json
from discord import app_commands
from discord.ext import commands

# input: local vars
intents = discord.Intents.default()
intents.message_content = True
bot_key = constants.discord_bot_key
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# process: declare async command function
@tree.command(name="apex_search", description="Search multiplayer stats for Apex Legends", guild=discord.Object(id=constants.discord_guild_id))
async def apex_search(ctx: discord.Interaction, player: str):
    if not (player):
        await ctx.respond.send_message('No player entered; try again with entry of player name.')
    else:
        results = player_search.main(player)
        print(type(results))
        print(len(results))
        for res in results:
            title = res
            description = results[res]
            description = str(description).replace("{","").replace("}","")
            em=discord.Embed(title=title, description=description)
            await ctx.channel.send(embed=em)

# process: declare async ready function
@client.event
async def on_ready():
    print(f'Bot has logged in as {client.user}')
    await tree.sync(guild=discord.Object(id=constants.discord_guild_id))

client.run(bot_key)