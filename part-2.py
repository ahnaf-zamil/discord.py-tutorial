import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Ready!\nUsername: {bot.user}")


@bot.event
async def on_message(message):
    print(f"{message.author} has sent a message.")


@bot.event
async def on_member_join(member):
    print(f"{member} has joined the server.")


@bot.event
async def on_member_remove(member):
    print(f"{member} has left the server.")

bot.run('token')
