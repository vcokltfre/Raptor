from bot.components.bot import Raptor

from .internal import InternalLogging


def setup(bot: Raptor) -> None:
    bot.add_cog(InternalLogging(bot))
