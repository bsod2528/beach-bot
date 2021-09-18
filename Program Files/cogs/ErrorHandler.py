"""

If you are not using this inside a cog, add the event decorator e.g:
@bot.event
async def on_command_error(ctx, error)
For examples of cogs see:
https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
For a list of exceptions:
https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#exceptions

"""
import discord
import traceback
from discord.ext import commands
import logging


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        logger = logging.getLogger('bitchlog')
        logger.setLevel(logging.DEBUG)
        logger.info("Error Handler Logged in")
        self.logger = logger

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member. Please try again.')
        
        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.qualified_name == "embedrandom": # -> you can use if blocks inside to give specific errors for different commands
                await ctx.send("I'm missing embed permissions")

        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            traceback_error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
            self.logger.error(f"Ignoring exception in command {ctx.command}:\nCommand Used - {ctx.message.content}\n{error}\n{traceback_error}")
            embed = discord.Embed(title="Command Error!",description=f"This error has been forwarded to the bot developer and will be fixed soon.\nDo not spam errored commands, doing so will get you blacklisted.",colour=discord.Colour.red())
            embed.add_field(name = "**Error:**", value= f"```py\n{error}```")
            try:
                #we try to send an embed
                await ctx.send(embed=embed)
            except:
                #if we're unable to send an embed then we send it as a message
                await ctx.send(f"**{embed.title}**\n{embed.description}\n\n**{embed.fields[0].name}**\n{embed.fields[0].value}")

    """Below is an example of a Local Error Handler for our command 'say' """

    @commands.command(name='say', aliases=['copy', 'print'])
    async def say(self, ctx, *, inp: str):
        """A simple command which repeats your input!
        Parameters
        ------------
        inp: str
            The input you wish to repeat.
        """
        await ctx.send(inp)

    @say.error
    async def sayerror(self, ctx, error):
        """A local Error Handler for our command 'say'.
        This will only listen for errors in 'say'.
        The global on_command_error will still be invoked after.
        """

        # Check if our required argument inp is missing.
        #commands.MissingRequiredArgument -> this is the error type
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")
                return
        traceback_error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
        self.logger.error(f"Ignoring exception in command {ctx.command}:\nCommand Used - {ctx.message.content}\n{error}\n{traceback_error}")

    
    async def cog_command_error(self, ctx, error):
        """ 
        This is an example a cog sepcific error handler
        This works same as the other Error handlers and 
        manages all th errors in that specific cog it is in only
        """
        traceback_error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
        self.logger.error(f"Ignoring exception in command {ctx.command}:\nCommand Used - {ctx.message.content}\n{error}\n{traceback_error}")




def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))