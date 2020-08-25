import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

your_id = 123435678 # Your Discord user ID

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.listening, name="Discord.py"
    ))
    print("Ready")


def is_me(ctx):
    return ctx.message.author.id == your_id


@bot.command()
@commands.check(is_me)
async def hi(ctx):
    await ctx.send("Hi!")


bot.run('token')
