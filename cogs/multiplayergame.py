import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''@commands.command()
    async def reg(self, ctx):
        #channel = client.get_channel(991769174286282762)
        channel = 991769174286282762
        await channel.send(channel)'''

    '''@commands.command
    async def reg(self, ctx, args):
        channel = client.get_channel(id)
        await channel.send(args)'''

        
def setup(client):
    client.add_cog(Test(client))
    