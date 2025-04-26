import discord
from discord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="reload")
    async def reload(self, ctx: commands.Context, cogname: str):
        if ctx.author.id == 1335428061541437531:
            await self.bot.reload_extension(f"cogs.{cogname}")
            await ctx.message.add_reaction("🔄")
        return
    
    @commands.command(name="load")
    async def load(self, ctx: commands.Context, cogname: str):
        if ctx.author.id == 1335428061541437531:
            await self.bot.load_extension(f"cogs.{cogname}")
            await ctx.message.add_reaction("👆")
        return
    
    @commands.command(name="unload")
    async def unload(self, ctx: commands.Context, cogname: str):
        if ctx.author.id == 1335428061541437531:
            await self.bot.unload_extension(f"cogs.{cogname}")
            await ctx.message.add_reaction("👇")
        return
    
async def setup(bot):
    print("-> AdminCog")
    await bot.add_cog(AdminCog(bot))