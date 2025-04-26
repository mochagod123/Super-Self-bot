from dotenv import load_dotenv
load_dotenv()
import os
import sqlite3

import discord
from discord.ext import commands

class SuperSelfBot(commands.Bot):
    def __init__(self):
        super().__init__(os.getenv("PREFIX"), help_command=None)
        self.conn = sqlite3.connect("savedata.db")
        self.cur = self.conn.cursor()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS permuser (
            id INTEGER PRIMARY KEY,
            userid INTEGER
        )
        ''')

bot = SuperSelfBot()

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