import nextcord
from nextcord.ext import commands

PREFIX = "$"
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.command()
async def test(ctx):
    await ctx.send("Tested!")

@bot.command()
async def load(ctx, extensions):
    bot.load_extension(f"cogs.{extensions}")
    await ctx.send("loaded")


@bot.command()
async def unload(ctx, extensions):
    bot.unload_extension(f"cogs.{extensions}")
    await ctx.send("unloaded")


@bot.command()
async def reload(ctx, extensions):
    bot.unload_extension(f"cogs.{extensions}")
    bot.load_extension(f"cogs.{extensions}")
    await ctx.send("reloaded")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")