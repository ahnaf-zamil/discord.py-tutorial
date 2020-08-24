import discord
from discord.ext import commands
from datetime import datetime
import os

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.listening, name="Discord.py"
    ))
    print("Ready")


@bot.command()
async def squared(ctx, num: int):
    await ctx.send(num ** 2)


@squared.error
async def squared_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Give me a number to square.")
        return
    if isinstance(error, commands.BadArgument):
        await ctx.send("Give me an integer")
        return

bot.run('token')
