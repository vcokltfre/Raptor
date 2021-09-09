from discord.ext.commands import Cog, Context, FlagConverter, command, flag, is_owner

from bot.components.bot import Raptor


class ControlFlags(FlagConverter, delimiter=" ", prefix="--"):
    verbose: bool = flag(name="verbose", aliases=["v"], default=False)


class Control(Cog):
    def __init__(self, bot: Raptor) -> None:
        self.bot = bot

    @command(name="botstatus")
    @is_owner()
    async def on_internal_log(self, ctx: Context, *, flags: ControlFlags) -> None:
        if flags.verbose:
            await ctx.send(
                f"Bot is online. WS ping: {self.bot.latency*1000:.2f}ms\n"
                f"Logged in as {self.bot.user} ({self.bot.user.id})\n"  # type: ignore
                f"{len(self.bot.cogs)} cogs loaded."
            )
            return
        await ctx.send(f"Bot is online. WS ping: {self.bot.latency*1000:.2f}ms")
