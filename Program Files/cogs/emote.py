import discord
import os
import random
import asyncio
import datetime
import json
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

    @commands.command()
    async def jsonemote(self, ctx):
        emote = json.load(open(r'D:\AV\PC\Coding\Discord Bot\Beach\Program Files\emote.json'))
        # we import json module and load the dir for the json file here. 
        # for loading and opening we use a r string.
        # jsonemote = is the variable name given to emotes present inside *emote* variable.
        jsonemote = [f'{emote["frogworry"]}',
                     f'{emote["yeaboi"]}',
                     f'{emote["pokisalute"]}',
                     f'{emote["susyou"]}',
                     f'{emote["tf"]}',
                     f'{emote["whyme"]}',
                     f'{emote["lesgo"]}',
                     f'{emote["yoo"]}']
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.reply(f'Well this command is to show how to import emotes from a json file.\n {random.choice(jsonemote)}')
        # so while printing the emote, we give the random choice variable name, which is jsonemote in this case
        # note, all variables names can be changed cos.
        # THEYRE VARIABLES !!

def setup(bot):
    bot.add_cog(EmotePy(bot))
