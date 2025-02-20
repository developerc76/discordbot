#!/discordbot/.venv/bin/python3

import discord
from discord.ext import commands
import random
import assets

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# When the bot is ready
@bot.event
async def on_ready():
    print(f'Successful login in as {bot.user}')

# !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# !ping
@bot.command()
async def ping(ctx):
    x = ctx.message.created_at
    message = await ctx.send("Waiting...")
    latency = (message.created_at - x).total_seconds() * 1000
    await message.edit(content=f'The bot has responded in {latency} seconds')

# !inspire
@bot.command()
async def inspire(ctx):
    x = assets.quote()
    quote = random.choice(x)
    await ctx.send(f"{quote}")

# !emoji
@bot.command()
async def emoji(ctx):
    emojis = assets.emoji()
    if ctx.author == "person614":
        await ctx.send("[Henry@ArchVM~]$ echo i use arch btw")
        return 0
    x = random.choice(emojis)
    await ctx.send(f"Your emoji is {x}. ")

# !code
@bot.command()
async def code(ctx):
    websites = assets.codesite()
    x: str = random.choice(websites)
    await ctx.send(f"Please click on the link or read the message: {x}")

# !feelinglucky
@bot.command()
async def feelinglucky(ctx):
    choices = assets.feelingLucky()
    message = await ctx.send("Waiting for bot to respond")
    for i in choices:
        message.edit(content=i)
    message.edit(content={random.choice(choices)})

# !hi
@bot.command()
async def hi(ctx):
    channel_members = [member for member in ctx.channel.members if not member.bot]
    await ctx.send(f"{random.choice(channel_members).mention}, {ctx.author.mention} says hello!")

bot.run('BOT_TOKEN')