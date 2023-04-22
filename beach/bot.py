from typing import List

import discord
import dotenv
from discord.ext import commands
from dotenv import dotenv_values

from .ext.help import MinimalHelp

dotenv.load_dotenv()

CONFIG = dotenv_values("config.env")
TOKEN = CONFIG.get("TOKEN")


EXTENSIONS: List[str] = [
    "jishaku",
    "beach.ext.fun",
    "beach.ext.developer",
    "beach.ext.errorhandler",
]


class BaseBeach(commands.Bot):
    """Subclass of `class`: `commands.Bot`."""

    def __init__(self, *args, **kwargs):
        super().__init__(
            status=discord.Status.idle,
            intents=discord.Intents.all(),
            activity=discord.Activity(
                type=discord.ActivityType.playing, name="Getting ready!"
            ),
            command_prefix=[".b"],
            case_insensitive=True,
            strip_after_prefix=True,
            *args,
            **kwargs,
            help_command=MinimalHelp(),
        )

        self.colour = discord.Colour.from_rgb(255, 100, 100)

    def __repr__(self) -> str:
        return "BaseBeach"

    async def load_exts(self):
        try:
            for ext in EXTENSIONS:
                await self.load_extension(ext)
        except Exception as error:
            print(error)

    async def setup_hook(self) -> None:
        await self.load_exts()
        self.tree.copy_global_to(guild=discord.Object(id=CONFIG.get("BSODsThings")))

    async def on_ready(self):
        return print(f"{self.user} - is now online!")


beachs_instance = BaseBeach()


async def run():
    """Starts the bot instance!"""
    async with beachs_instance:
        await beachs_instance.start(TOKEN)
