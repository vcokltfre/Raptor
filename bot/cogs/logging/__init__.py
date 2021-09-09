from bot.components.bot import Raptor

from .guilds import GuildLogging
from .internal import InternalLogging


def setup(bot: Raptor) -> None:
    bot.add_cog(InternalLogging(bot))
    bot.add_cog(GuildLogging(bot))
