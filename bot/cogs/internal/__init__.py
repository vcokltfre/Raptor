from bot.components.bot import Raptor

from .control import Control


def setup(bot: Raptor) -> None:
    bot.add_cog(Control(bot))
