from ...bot import BaseBeach
from .fun import Fun


async def setup(bot: BaseBeach):
    await bot.add_cog(Fun(bot))
