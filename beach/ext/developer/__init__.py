from ...bot import BaseBeach
from .developer import Developer


async def setup(bot: BaseBeach):
    await bot.add_cog(Developer(bot))
