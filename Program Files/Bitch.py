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
# THE PRINT GIVEN ABOVE PRINTS IN OUR CONSOLE THAT THE BOT IS UP AND GOOD TO RUN

# COGS SETUP
for filename in os.listdir('D:\AV\PC\Coding\Discord Bot\Beach\Program Files\cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Before giving the pathway, we make a separate folder called *cogs*. This is where all our cogs will be stored.
# For our bot to recognize the cogs in our cogs folder, we have written code from lines 21 to 23
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

# Make sure the bot logs in 
bot.run('Token')