import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Ready!\nUsername: {bot.user}")


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000, 2)
    await ctx.send(f"{latency} ms")


@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)


@bot.command()
async def info(ctx, age, color, *, name):
    await ctx.send(f"Age: {age}\nColor: {color}\nName: {name}")

bot.run('token')
