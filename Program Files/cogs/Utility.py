import inspect
import discord
from discord.ext import commands
import os


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases  = ['src'])
    async def source(self, ctx, *, command: str = None):
        """Displays my full source code or for a specific command.
        To display the source code of a subcommand you can separate it by
        periods, e.g. tag.create for a create subcommand of the tag command
        or by spaces.
        """
        view = discord.ui.View()
        source_url = 'https://github.com/BSOD2528/Beach-Bot'
        #Github link to the source code repo
        branch = 'main'
        #The branch which the current repo uses
        emoji = "<:github:889018277815279676>"
        #Make sure to replace the emoji with one that your bot is in, incase it isn't in Woodlands

        if command is None:
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url = source_url, label = "Source", emoji = emoji))
            return await ctx.send("Here's the Entire Repo", view = view)

        if command == 'help':
            src = type(self.bot.help_command)
            module = src.__module__
            filename = inspect.getsourcefile(src)
        else:
            obj = self.bot.get_command(command.replace('.', ' '))
            if obj is None:
                return await ctx.send(f'Could not find command: {command}')

            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            module = obj.callback.__module__
            filename = src.co_filename

        lines, firstlineno = inspect.getsourcelines(src)
        if not module.startswith('discord'):
            # not a built-in command
            location = os.path.relpath(filename).replace('\\', '/')
        else:
            location = module.replace('.', '/') + '.py'

        final_url = f'{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}'.replace(" ","%20")
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url = final_url, label = "Source", emoji = emoji))
        await ctx.send(f"Here's the source for `{command}`", view = view)

def setup(bot):
    bot.add_cog(Utility(bot))