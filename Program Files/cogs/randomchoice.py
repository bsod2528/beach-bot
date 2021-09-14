# importing modules in cogs is necessary for them to work too!!
import discord
import random
import os
import datetime
import asyncio
from discord.ext import commands

# this is how you start a cog, by creating a class and naming the class 
# classes are supposed to be there in each cog beginining, otherwise that isnt a cog!
# the name of your class will be the name of your cog. Note that down, and thank me later

class RandomChoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # we define that self.bot is bot as inside a cog, self is necessary to be used

    @commands.command()
    async def cogexample(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send('This is a simple command for which is present in a cog')
    # in cogs, an indent has to be given so that they are present inside the cog properly.
    # @commands.command() --> way to begin a command in a cog
    # in command decorator, self has to be added ( as the command is inside a cog )

    # random output
    @commands.command(alias = ['re'])
    async def randomexample(self, ctx):
        random_output = ['Random A',
                         'Random B',
                         'Random C',
                         'Random D']
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send(f'{random.choice(random_output)}')
    # random_output --> this is a variable name set to the random output variable.
    # f string is utilised so that the random choice works.


    # same random output, but in an embed
    @commands.command(alias = ['er'])
    async def embedrandom(self, ctx):
        embed_random_output = ['Random 1',
                               'Random 2',
                               'Random 3',
                               'Random 4']
        emb = discord.Embed(
            title = 'Random in Embed',
            description = 'This embed will consist a random output below.\n'
                          '{random.choice(embed_random_output)}')
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send(embed = emb)
    # the {random.choice(variable)} is supposed to be mentioned in description, as thats where all the main content goes.
    # as usual, we send the embed the ctx.send and hence we get our output ( when command is invoked ) as an embed.

def setup(bot):
    bot.add_cog(RandomChoiceCog(bot))
# this is called as the setup function ( aka setup func. )
# make sure you have this in all your cog endings. This will setup the cog.