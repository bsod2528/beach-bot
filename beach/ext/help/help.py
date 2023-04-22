import discord
from discord.ext import commands


class MinimalHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()

        for page in self.paginator.pages:
            emb = discord.Embed(
                title="Beach Bot is here to Help", description=page, color=0xFF6464
            )
            emb.timestamp = discord.utils.utcnow()
            await destination.send(embed=emb)
