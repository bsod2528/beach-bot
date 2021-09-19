import inspect
import discord
from discord.ext import commands
import os


class Utility(commands.Cog):
    """ Some basic Utility Commands """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "ping", help = "View the ping of the bot", brief = "Take a wild guess")
    @commands.guild_only()
    #This restricts the command to be run only in guilds, the opposite being only dms would require the `@commands.dm_only()` decorator
    async def ping(self, ctx):
        #Basic ping command which gives the bot latency
        await ctx.reply(f"Pong!\nMy Ping is `{round(self.bot.latency*1000)} ms`")
    
    @commands.command(name = "about", help = "View some info about the bot", brief = "Get Bot Info", aliases = ['info', "botinfo"])
    @commands.guild_only()
    async def about(self, ctx):
        dev = self.bot.get_user(750979369001811982)
        contributers = [760823877034573864]
        contributers = [self.bot.get_user(us) for us in contributers]
        #Here we get the all the users who contributed
        colour = ctx.me.colour if ctx.me.colour != "#000000" else discord.Colour.random()
        #Set the colour to the bots top role colour or a random colour if it doesn't have any colour
        embed = discord.Embed(title="About Beach Bot", description = f"Beach Bot is a public bot made to be a fun and simple template / guide on how to create an amazing DISCORD BOT using Python Language. Click the Button below to take a look at the source code repo. This bot and its source code repository is made and maintained by **[{dev}]({dev.avatar})**\n\u200b", colour = colour)
        embed.set_thumbnail(url=ctx.me.avatar)
        embed.add_field(name="Other Contributers:",value="\n".join([f"**[{user}]({user.avatar})**" for user in contributers]))
        embed.add_field(name="Coded in:",value=f"**Language:** **[`python 3.8.5`](https://www.python.org/)**\n**Library:** **[`discord.py 2.0`](https://github.com/Rapptz/discord.py)**\nㅤㅤㅤㅤ\U00002514 Master Branch")
        #Add info about what the bot is coded in

        #Get some more additions stats about the Bot
        embed.add_field(name="Statistics:",value=f"**Servers:** {len([g.id for g in self.bot.guilds])} servers\n**Users:** {len([g.id for g in self.bot.users])}", inline = False)
        embed.add_field(name="On Discord Since:",value=f"<t:{round(ctx.me.created_at.timestamp())}:D>")
        #we'll now add a link button to the source code repo
        view = discord.ui.View()
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url = 'https://github.com/BSOD2528/Beach-Bot', label = "Github Repo", emoji = "<:github:889018277815279676>"))
        await ctx.send(embed = embed, view = view)

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
        
        obj = self.bot.get_command(command.replace('.', ' '))

        if command == 'help':
            src = type(self.bot.help_command)
            module = src.__module__
            filename = inspect.getsourcefile(src)
        else:
            if obj is None:
                return await ctx.send(f'Could not find command: {command}')


            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            module = obj.callback.__module__
            filename = src.co_filename

        lines, firstlineno = inspect.getsourcelines(src)
        if not module.startswith('discord') or command == 'help':
            # not a built-in command
            location = "Program Files" + os.path.relpath(filename).replace('\\', '/').split("Program Files")[-1]
        else:
            location = module.replace('.', '/') + '.py'
        final_url = f'{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}'.replace(" ","%20")
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url = final_url, label = "Source", emoji = emoji))
        await ctx.send(f"Here's the source for `{obj.qualified_name}`", view = view)

def setup(bot):
    bot.add_cog(Utility(bot))
