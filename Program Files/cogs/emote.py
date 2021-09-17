import discord
import os
import random
import asyncio
import datetime
from discord.ext import commands

# you do not require to import any new module for sending emotes!.

# to get emote id add \ before typing out the emote
# example, emote name is bruhh. We get id by
# \:bruhh: and then sending the message in a channel.

# note that these emotes are present in the server which your bot is in too!

class EmotePy(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    # a command to give out emotes
    @commands.command(alias = ['et'])
    async def emotetest(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send(f'Normal Static Emote -> <:frogworry:887502713976410165>')
    
    # another example, but this time its and animated emote
    @commands.command(alias = ['at'])
    async def aniemote(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send(f'Animated Emote --> <a:pepehehe:877959535137026059>')
    
    # a simple embed which outputs a random emote in an embed.
    @commands.command()
    async def embedemote(self, ctx):
        emote = ['<a:pepehehe:877959535137026059>',
                 '<:frogworry:887502713976410165>',
                 '<:linusbruh:885886169320140880>',
                 '<:linusfocboi:885886954078625793>',
                 '<:linuskill:886606006761717760>',
                 '<a:trumpisclap:887740398020223006>']
        emb = discord.Embed(
            title = 'Emote Embed',
            description = f'{random.choice(emote)}',
            color = ctx.author.color)
        emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send(embed = emb  )

def setup(bot):
    bot.add_cog(EmotePy(bot))
