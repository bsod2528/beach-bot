from ...bot import BaseBeach
from .errorhandler import CommandErrorHandler


async def setup(bot: BaseBeach):
    await bot.add_cog(CommandErrorHandler(bot))
