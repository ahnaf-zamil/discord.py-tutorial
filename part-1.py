import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Ready!\nUsername: {bot.user}")

bot.run('YOUR TOKEN')
