import discord
from discord.ext import commands

class BotCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help")
    @commands.cooldown(2, 10, type=commands.BucketType.user)
    async def help(self, ctx: commands.Context):
        await ctx.reply("""```
User: help

Prefix: ['!?']
```""")
        return

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, err: commands.CommandError):
        if isinstance(err, commands.CommandOnCooldown):
            e = 0
            return e
        else:
            await ctx.message.add_reaction("❌")
            await self.bot.get_channel(1365657658476072981).send(content=f"```{err}```")
            return
        
    @commands.Cog.listener("on_message")
    async def on_message_command(self, message: discord.Message):
        if message.author.bot:
            return
        
        await self.bot.process_commands(message)

async def setup(bot):
    print("-> BotCog")
    await bot.add_cog(BotCog(bot))