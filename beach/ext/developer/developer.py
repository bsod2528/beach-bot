from typing import Optional

from discord import Message
from discord.ext import commands

from ...bot import BaseBeach


class Developer(commands.Cog):
    def __init__(self, bot: BaseBeach) -> None:
        self.bot = bot

    @commands.command(name="load", aliases=["l"], brief="Load a cog")
    @commands.is_owner()
    async def load(self, ctx: commands.Context, *, cog: str) -> Optional[Message]:
        """Load a cog!"""
        try:
            await self.bot.load_extension(f"beach.ext.{cog}")
            return await ctx.send(f"Successfully `loaded` - **{cog}**!")
        except Exception as error:
            await ctx.send(
                f"There was an error in loading the cog:\n```py\n{error}\n```"
            )

    @commands.command(name="unload", aliases=["ul"], brief="Unload a cog")
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, *, cog: str) -> Optional[Message]:
        """Unload a cog!"""
        try:
            await self.bot.unload_extension(f"beach.ext.{cog}")
            return await ctx.send(f"Successfully `unloaded` - **{cog}**!")
        except Exception as error:
            await ctx.send(
                f"There was an error in unloading the cog:\n```py\n{error}\n```"
            )

    @commands.command(name="reload", aliases=["rl"], brief="Reload a cog")
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, *, cog: str) -> Optional[Message]:
        """Reload a cog!"""
        try:
            await self.bot.reload_extension(f"beach.ext.{cog}")
            return await ctx.send(f"Successfully `reloaded` - **{cog}**!")
        except Exception as error:
            await ctx.send(
                f"There was an error in reloading the cog:\n```py\n{error}\n```"
            )
