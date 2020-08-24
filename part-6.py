import discord
from discord.ext import commands
from datetime import datetime
import os

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name="Test"
    ))
    print("Ready")

bot.run('token')
