import discord
from discord.ext import commands
from datetime import datetime

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


@bot.command()
async def sendembed(ctx):
    embed = discord.Embed(
        title="Test Embed",
        color=discord.Color.blue(),
        description="Some description that I wrote without even thinking about it."
    )
    embed.add_field(
        name="Field 1", value="This is the 1st inline field.", inline=True)
    embed.add_field(
        name="Field 2", value="This is the 2nd inline field.", inline=True)
    embed.add_field(
        name="Field 3", value="This is the 3rd inline field,", inline=False)
    embed.set_image(url="https://i.stack.imgur.com/8xAac.png")
    embed.set_thumbnail(url="https://i.stack.imgur.com/8xAac.png")
    embed.set_author(name="Author's name", icon_url=bot.user.avatar_url)
    embed.set_footer(text="This is a footer", icon_url=bot.user.avatar_url)
    embed.timestamp = datetime.utcnow()
    await ctx.send(embed=embed)

bot.run('token')
