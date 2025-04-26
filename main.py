from dotenv import load_dotenv
load_dotenv()
import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=os.getenv("PREFIX"), help_command=None)

@bot.event
async def on_ready():
    print("Ready.")

@bot.event
async def on_message(message):
    return

@bot.event
async def setup_hook():
    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")

bot.run(os.getenv("TOKEN"))