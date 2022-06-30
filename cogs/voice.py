import discord
from discord.ext import commands
import json
import requests

class VoiceCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def youtube(self, ctx):
        data={
            "max_age": 86400,
            "max_uses": 0,
            "target_application_id": 755600276941176913,
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers={
            "Authorization": "Bot ODQ3NzYyMjI5MTY3OTE1MDE4.YLCyGg.of6YcyMideruwWRpK0JnBzaX6KM",
            "Content-Type": "application/json"
        }
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в голосовой канал")
        else:
            await ctx.send("Зайдите в голосовой канал")
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)

        await ctx.send(embed = discord.Embed(title=f"Нажмите на ссылку чтобы войти в приложение: https://discord.com/invite/{link['code']}"))
    @commands.command()
    async def chess(self, ctx):
        data={
            "max_age": 86400,
            "max_uses": 0,
            "target_application_id": 832012774040141894,
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers={
            "Authorization": "Bot ODQ3NzYyMjI5MTY3OTE1MDE4.YLCyGg.of6YcyMideruwWRpK0JnBzaX6KM",
            "Content-Type": "application/json"
        }
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в голосовой канал")
        else:
            await ctx.send("Зайдите в голосовой канал")
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)

        await ctx.send(embed = discord.Embed(title=f"Нажмите на ссылку чтобы войти в приложение: https://discord.com/invite/{link['code']}"))
            






    
    @commands.Cog.listener()
    async def on_ready(self):
        print('[Система] Группа VoiceCommands авторизована')
        print('------')
        #await bot.change_presence( status = discord.Status.online, activity = discord.Game( '@PersikBot help' ) )   
def setup(client):
    client.add_cog(VoiceCommands(client))