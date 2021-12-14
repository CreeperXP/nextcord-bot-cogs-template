import nextcord
from nextcord.ext import commands

class hello_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Hello(self, ctx):
		await self.ctx.send("Hi!")


def setup(bot):
    bot.add_cog(hello_command(bot))