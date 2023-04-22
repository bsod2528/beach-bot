from typing import Optional

import discord
from discord import Message, app_commands
from discord.ext import commands

from ...bot import BaseBeach
from ...views.source import RepoLink


class Fun(commands.Cog):
    def __init__(self, bot: BaseBeach):
        self.bot = bot
        self.first_context_menu = app_commands.ContextMenu(
            name="Who is This!", callback=self.who_is_this
        )
        self.second_context_menu = app_commands.ContextMenu(
            name="Message Sent At", callback=self.when_was_this_sent
        )
        self.bot.tree.add_command(self.first_context_menu)
        self.bot.tree.add_command(self.second_context_menu)

    async def who_is_this(
        self, interaction: discord.Interaction, user: discord.User | discord.Member
    ):
        return await interaction.response.send_message(
            content=f"The user you've selected is **{user}**", ephemeral=True
        )

    async def when_was_this_sent(
        self, interaction: discord.Interaction, message: Message
    ):
        return await interaction.response.send_message(
            content=f"This message was sent on: {discord.utils.format_dt(message.created_at, style='D')} | {discord.utils.format_dt(message.created_at, style='R')}"
        )

    @commands.command(name="source", aliases=["src"], brief="Get source for commands!")
    async def repo(self, ctx: commands.Context) -> Optional[Message]:
        await ctx.send(f"My Source Code:", view=RepoLink())
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(label="Links Utilised", url="https://cutt.ly/yEtYbBn")
        )
        await ctx.send(f"Links Utilised:", view=view)

    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction) -> Optional[Message]:
        """Nothing, I just ping!"""
        return await interaction.response.send_message(
            content=f"Pong {interaction.user}!", ephemeral=True
        )

    @commands.command(name="spoiler", brief="Spoiler a message")
    async def spoiler(self, ctx: commands.Context, *, string: str) -> Optional[Message]:
        """Spoil a message!"""
        return await ctx.send("".join(f"||{var}||" for var in string))
