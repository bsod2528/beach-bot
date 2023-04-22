"""

If you are not using this inside a cog, add the event decorator e.g:
@bot.event
async def on_command_error(ctx, error)
For examples of cogs see:
https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
For a list of exceptions:
https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#exceptions

"""
import traceback

import discord
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        if hasattr(ctx.command, "on_error"):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound,)
        error = getattr(error, "original", error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f"{ctx.command} has been disabled.")

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(
                    f"{ctx.command} can not be used in Private Messages."
                )
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            await ctx.send("I could not find that member. Please try again.")

        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.qualified_name == "embedrandom":
                await ctx.send("I'm missing embed permissions")

        else:
            embed = discord.Embed(
                title="Command Error!",
                description=f"This error has been forwarded to the bot developer and will be fixed soon.\nDo not spam errored commands, doing so will get you blacklisted.",
                colour=discord.Colour.red(),
            )
            embed.add_field(name="**Error:**", value=f"```py\n{error}```")
            try:
                await ctx.send(embed=embed)
            except:
                await ctx.send(
                    f"**{embed.title}**\n{embed.description}\n\n**{embed.fields[0].name}**\n{embed.fields[0].value}"
                )

    """Below is an example of a Local Error Handler for our command "say" """

    @commands.hybrid_command(name="say", aliases=["copy", "print"])
    async def say(self, ctx, *, inp: str):
        """A simple command which repeats your input!"""
        await ctx.send(inp)

    @say.error
    async def sayerror(self, ctx, error):
        """A local Error Handler for our command "say".
        This will only listen for errors in "say".
        The global on_command_error will still be invoked after.
        """

        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == "inp":
                await ctx.send("You forgot to give me input to repeat!")
                return
