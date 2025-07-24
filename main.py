import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.intents.default()
intents.message_content = True

bot = commands.Bot(commands_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Conectado como (bot.user.name)")

@bot.command()
async def hola(ctx):
    await ctx.send("Hola soy tu bot de juegos gratis")

async def ping(ctx)
    await ctx.send("estoy vivo")

bot.run(TOKEN)