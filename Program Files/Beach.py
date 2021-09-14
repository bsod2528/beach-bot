# where we import modules necessary for our bot
import discord
import random 
import datetime
import os
import asyncio
from discord import activity
from discord.enums import Status
from discord.ext import commands

# bot constructor
bot = commands.Bot(command_prefix = '.b', status = discord.Status.idle, activity = discord.Game(name = 'Just a Bitch ;)') )
Token = # your bot token [ CHECK DISCORD DEVELOPER PORTAL ] 

# bot login confirmation into discord
@bot.event
async def on_ready():
    print('Bitch Im REAADDDYYY!!!')
# the print given above prints it in the console when you run the bot

# COGS SETUP
for filename in os.listdir('D:\AV\PC\Coding\Discord Bot\Beach\Program Files\cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# before giving the pathway, we make a separate folder called *cogs*. This is where all our cogs will be stored.
# for our bot to recognize the cogs in our cogs folder, we have written code from lines 21 to 23
# os.listdr --> it is the directory present in our OS ( OPERATING SYSTEM ).
# We give out the directory for our *cogs* folder and paste it in line 21.
# bot.load_extension --> this command will load all the cogs into usage and hence there will be no problem.

# bot.unload_extension ( not given in code, but for FYI ) --> this is unload that particular cog you select / give in as a command and hence 
# you will be forced to load it again to use that cog


# command in the main bot.py
@bot.command
async def bich(ctx):
    await ctx.send('Ye, I know your a bich. \n'
                    '*heads out silently*')
# ctx --> context
# all it does is represents the context in which a command is being invoked under.
# you always do await to give output and *ctx.send* --> sends the context to the place where you have invoked the command

@bot.command
async def bichy(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await ctx.send('Stop being so bitchy EWWW!!!!')
# async with ctx.typing --> all it does is it asynchronises with the context being typed sent where the command is invoked
# await asyncio.sleep(0.5) --> it waits for the time ( sleep ) as when typing we take some time to write down the words, this replicates it.

@bot.command
async def embed(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    emb = discord.Embed(
        title = 'This is the title of the Embed',
        description = 'You add descriptions for the embed here. You can add more content by\n'
                       'Using New Line',
        color = ctx.author.color)
# this is how one creates an embed. More colors will be present in ReadMe, check it out!

    emb.add_field(
        name = 'This is the title for a field',
        value = 'Description for a field is given by value',
        inline = False)
# inline False is given, otherwise your embed will look bazinga boing! 
# its your own personal preference, I like embeds with inline as False, experiment and see what you get without the inline value given. You'll knwo what I mean.
# no need to mention *Color* as these are only extra fields for your embed above.

    await ctx.send(embed = emb)
# you send your embed with ctx. Note to point, I have given emb, you guys can add whatever you want to. emb is only a variable name for the embed on the whole.


# make sure the bot logs in 
bot.run('Token')