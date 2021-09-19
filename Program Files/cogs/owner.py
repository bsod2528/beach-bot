from logging import exception
import discord
import os
import asyncio
import datetime
from discord.ext import commands

# this cog is specifically for the bot owner
class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # initialisation finished for the cog 

    # the load command is used to load cogs into usage ( if the cogs has been unloaded )

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)
        #Cog Checks are like normal command checks except that they apply to the whole cog
        #In this case we Check if the user is the bot Owner
        #This makes it easier to check without having to add one for every single command in this cog

    # is_owner() --> a check which the bot will run, to see whether if the person who invoked the command is the bot owner or not.
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'*`ERROR:`*{type(e).__name__} - {e}')
        else:
            await ctx.send(f'*`Done`*')
    # what happens here is, we give options to the bot. If we input the right cog file name, it will load the cog for us.
    # otherwise, an error will pop up ( line 21 )
    # if we do give the right name and everything, the bot will respond with line 23 i.e, DONE.
    # this is used to bring back cogs for using ( invoking commands present inside them )

    # the same can be done for unload cogs.
    @commands.command()
    async def unload(self, ctx, *, cog : str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`**{type(e).__name__} - {e}')
        else:
            await ctx.send(f'**`Done`**')
    # when we unload certain cogs, the cog will not be present for using commands inside and those commands would not work at all.
    # note that, if we unload OwnerCog, we will not be able to utilise commands inside them and hence. We have a workaround for this.
    # workaround for this particular thing will be shown later.


    #This does the same thing is used to reload loaded cogs by unloading them and loading them in one single command
    @commands.command()
    async def reload(self, ctx, *, cog : str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`**{type(e).__name__} - {e}')
        else:
            await ctx.send(f'**`Done`**')

    # this is for enabling and disabling certain commands present inside any cog.
    @commands.command(name="toggle", description="Enable or disable a command!", alias = ['tg'])
    async def toggle(self, ctx, *, command):
        command = self.bot.get_command(command)
    # the astericks or * given states that this is will take in input from the user for n number of characters ( i.e, infinite characters )
        if command is None:
            emb = discord.Embed(
                title = 'ERROR', 
                description = 'I cant find a command with that name!', 
                color = ctx.author.color)
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            async with ctx.typing():
                await asyncio.sleep(0.5)
            await ctx.send(embed=emb)
    # if we do not send a command name after the `toggle` or give a wrong command name, we get and error
        
        elif ctx.command == command:
            emb = discord.Embed(
                title = 'ERROR', 
                description = 'You cannot disable this command.', 
                color =ctx.author.color)
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            async with ctx.typing():
                await asyncio.sleep(0.5)
            await ctx.send(embed=emb)
    # this is a small error handler, that is if someone else tried to toggle any commands, they will get this result.

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            emb = discord.Embed(
                title = 'Toggle',
                description = f'I have {ternary} {command.qualified_name} for you!',
                color = ctx.author.color)
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            async with ctx.typing():
                await asyncio.sleep(0.5)
            await ctx.send(embed=emb)
    # this is the output we get when WE as the owner of bot, toggle a command.

    # as you can see, we have added emb.timestamp in each of our embeds. 
    # the timestamp will provide the time at which the time at which the command was invoked. 
    # for this to occur, we have imported a module named *datetime* ( check line 5 of this cog ).


    #Its always better to close the bot using await bot.close() rather than closing the file that you're running
    @commands.command(name="shutdown", aliases = ['die','stop'], help = "Shutdown the bot in a peaceful way, rather than just closing the window", brief = "Shutdown ")
    async def shutdown(self, ctx):
        await ctx.reply("Shutting down")
        try:
            #Here the bot tries to add a reaction if possible, else it just ignores and passes
            await ctx.message.add_reaction("\U00002705")
        except:
            pass
        await self.bot.close()
        #await self.bot.close closes the bot properly

def setup(bot):
    bot.add_cog(OwnerCog(bot))