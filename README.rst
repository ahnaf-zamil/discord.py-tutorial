# Discord.py Tutorial
==========
All of the code for the Discord.py tutorial on my channel are available in this repository

## Installing Discord.py
-------------
**Python 3.5.3 or higher is required**

.. code:: sh

     pip install discord
     

Bot Example
~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='>')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')
