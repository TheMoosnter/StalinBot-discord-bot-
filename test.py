import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, arg, amount=1):
        await ctx.channel.purge(limit=amount)
        await ctx.send(arg)

        
def setup(client):
    client.add_cog(Test(client))
    