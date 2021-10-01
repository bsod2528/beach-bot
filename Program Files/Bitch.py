# where we import modules necessary for our bot
import discord
import random 
import datetime
import pathlib
import os
import asyncio
from discord.ext import commands
import logging
import json

# bot constructor

#@e're subclassing the bot for better processing
class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix= [".b"],  intents = discord.Intents.all(), status = discord.Status.idle, activity = discord.Game(name = '.b | Just a Bitch ;)'))
        #Here we mention intents = discord.Intents.all() so as to utilise all the intents, can be changed as required
    
    async def on_ready(self):
        # bot login confirmation into discord

        #Bunch of info stuff being logged to the console
        print(f'\n\nLogged in as {self.user} (ID: {self.user.id})')
        total_members = list(bot.get_all_members())
        total_channels = sum(1 for x in bot.get_all_channels())
        print(f'Guilds: {len(bot.guilds)}')
        print(f'Large Guilds: {sum(g.large for g in bot.guilds)}')
        print(f'Chunked Guilds: {sum(g.chunked for g in bot.guilds)}')
        print(f'Members: {len(total_members)}')
        print(f'Channels: {total_channels}')
        print(f'Message Cache Size: {len(bot.cached_messages)}\n')
        print('\nBitch Im REAADDDYYY!!!')
        # the print statements given above prints it in the console when you run the bot

bot = Bot()

token = json.load(open(r'D:\AV\PC\Coding\Discord Bot\Beach\Program Files\config.json')) 
# your bot token [ CHECK DISCORD DEVELOPER PORTAL ] 

rootdir = pathlib.Path(__file__).parent.resolve()

# Loggers help keep your console from being flooded with Errors, you can instead send them to a file which you can check later
logger = logging.getLogger('bitchlog')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=f'{rootdir}/bitchlog.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logger.info("Bitch Bot is online")


# COGS SETUP
for filename in os.listdir(f'{rootdir}/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# before giving the pathway, we make a separate folder called *cogs*. This is where all our cogs will be stored.
# for our bot to recognize the cogs in our cogs folder, we have written code from lines 21 to 23
# os.listdr --> it is the directory present in our OS ( OPERATING SYSTEM ).
# We give out the directory for our *cogs* folder and paste it in line 21.
# bot.load_extension --> this command will load all the cogs into usage and hence there will be no problem.

# bot.unload_extension ( not given in code, but for FYI ) --> this is unload that particular cog you select / give in as a command and hence 
# you will be forced to load it again to use that cog


# this is a minimal help command example. More links for help commands have been given in ReadMe.md in main repo!
class MinimalHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()

# so we create a class mentioning the name for our help command.
# this is only a mininmal help command!        
# make sure you guys add the help text for each command and category.
        
        for page in self.paginator.pages:
            emb = discord.Embed(
                title = 'Beach Bot is here to Help',
                description = page,
                color = 0x3498db)
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            # this is how you add a timestamp on your embed. For this datetime has to be imported
            await destination.send(embed = emb)

bot.help_command = MinimalHelp()

# command in the main bot.py
@bot.command(brief = 'A simple Command in Main.py')
async def beach(ctx):
    await ctx.send('Yeah, I love the beach!\n'
                    '*heads out silently*')

# ctx --> context
# all it does is represents the context in which a command is being invoked under.
# you always do await to give output and *ctx.send* --> sends the context to the place where you have invoked the command

@bot.command(brief = 'Showcases the power of ctx.typing()')
async def sandy(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await ctx.send('Stop being so beachy EWWW!!!!')

# async with ctx.typing --> all it does is it asynchronises with the context being typed sent where the command is invoked
# await asyncio.sleep(0.5) --> it waits for the time ( sleep ) as when typing we take some time to write down the words, this replicates it.

@bot.command(brief = 'A simple embed example in main.py')
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

# to send a button with a link, we have to create new class and give it a function called discord.ui.View
class RepoLink(discord.ui.View):
    def __init__(self):
        super().__init__()
        url = f'https://github.com/BSOD2528/Beach-Bot'
        self.add_item(discord.ui.Button(label = 'Beach Bot Repo', url = url))
        # self.add_item --> Here self denotes the class itself, in this case its the view (discord.ui.View). So self.add_item() adds the item to the Class.

@bot.command(brief = 'Sends a button with a link to the Public Repo')
async def repo(ctx: commands.Context):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await ctx.send(f'My Source Code:', view = RepoLink())
    #Here is another way to add views without using classes
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label = 'Links Utilised', url = 'https://cutt.ly/yEtYbBn'))
    await ctx.send(f'Links Utilised:', view = view)

# make sure the bot logs in 

bot.run(f'{token["TOKEN"]}')
