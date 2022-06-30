import discord
from discord.ext import commands
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
class TextCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('[Система] Группа TextCommands была авторизирована')
    @commands.command()
    async def serverEmbed(self, ctx,arg1,arg2, webhook: discord.Webhook = 'PB Webhook'):
        async with aiohttp.ClientSession() as session:
            avatar = ctx.guild.icon_url
            name = ctx.guild.name
            varible = await ctx.channel.create_webhook(name= 'PB Webhook')
            url = varible.url
            webhook1 = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            await webhook1.send(embed = discord.Embed(title = arg1, description = arg2), username=name, avatar_url = avatar)
            await varible.delete()
    @commands.command()
    async def botEmbed(self, ctx, arg1, arg2):
        emb11 = discord.Embed(title = arg1, description = arg2)
        await ctx.send( embed = emb11 )
    @commands.command()
    async def userEmbed(self, ctx,arg1,arg2, webhook: discord.Webhook = 'PB Webhook'):
        async with aiohttp.ClientSession() as session:
            avatar = ctx.author.avatar_url
            name = ctx.author.name
            varible = await ctx.channel.create_webhook(name= 'PB Webhook')
            url = varible.url
            webhook1 = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            await webhook1.send(embed = discord.Embed(title = arg1, description = arg2), username=name, avatar_url = avatar)
            await varible.delete()
    @commands.command()
    async def bot(self, ctx):
        emb11 = discord.Embed(title='Информация', description = 'Этот бот предназначен в основном для модерации и для игр. В боте доступно 2 префикса для выполнения команд. Это !~ и @PersikBot (упомянуть бота).Для ознакомления с командами пропишите @PersikBot help')
        await ctx.send( embed = emb11 )
        emb11 = discord.Embed(title = 'VKontante',url='https://vk.com/persikbotdiscord')
        await ctx.send( embed = emb11 )
        emb11 = discord.Embed(title = 'Discord',url='https://discord.com/invite/z3u53MF3jD')
        await ctx.send( embed = emb11 )
        emb11 = discord.Embed(title = 'Приглашение на сервер',url='https://discord.com/api/oauth2/authorize?client_id=810429775695839293&permissions=8&scope=bot')
        await ctx.send( embed = emb11 )
        
def setup(client):
    client.add_cog(TextCommands(client))