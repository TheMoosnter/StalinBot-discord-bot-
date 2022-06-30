import discord
from discord.ext import commands
from asyncio import sleep
import asyncio

class ModerCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('[Система] Группа ModerCommands была авторизирована')
    @commands.command( past_context = True)
    @commands.has_permissions( administrator = True )
    async def kick (self, ctx, member: discord.Member, *, arg):       
    #if On == 'True':
        reason = arg
        await member.kick( reason=reason )
        emd5 = discord.Embed(description = f'Пользователь {member.mention} был экстрадирован по причине { reason }',  colour = discord.Color.green())
        await ctx.send( embed = emd5 )
    @commands.command( pass_context = True)
    @commands.has_permissions( administrator = True )
    async def tempban(self, ctx, user:discord.User, duration: int, arg):
    #if On == 'True':
        reason = arg
        await ctx.guild.ban(user, reason = reason)
        dur = duration
        await ctx.send(embed = discord.Embed(title = 'Бан', description = f'Пользователь { user.mention } отправлен в Сибирь на { duration } секунд по причине: { reason }',  colour = discord.Color.green()))
        await asyncio.sleep(duration)
        await ctx.guild.unban(user)
    @commands.command( pass_context = True)
    @commands.has_permissions( administrator = True )
    async def ban(self, ctx, member: discord.Member, arg):
    #if On == 'True':
        await ctx.guild.ban(member, reason = arg)
        await ctx.send(embed = discord.Embed(title='Бан',description = f'Пользователь { member.mention } был уничтожен Сталиным по причине: {arg}',  colour = discord.Color.green()))
    @commands.command()   
    @commands.has_permissions( administrator = True )
    async def unban(self, ctx, user:discord.User):
    #if On == 'True':
        await ctx.guild.unban(user)
        await ctx.send(embed = discord.Embed(title='Разбан',description= f' {user.name} был разабанен ',  colour = discord.Color.green()))

    @commands.command()
    @commands.has_permissions( administrator = True )
    async def mute(self, ctx, member: discord.Member, duration: int, arg = None):
        reason = arg
        if arg == None:
            reason = "Причина не задана"

        if member.id == ctx.author.id:
            await ctx.send(embed = discord.Embed(title= "MUTE_ERROR", description="Вы не можете заглушить самого себя.", colour = discord.Color.green()))

        role = discord.utils.get(ctx.guild.roles, name="Напуган Сталиным")

        await member.add_roles(role)
        await ctx.send(embed = discord.Embed(title="Мут", description=f"Пользователь {member.name} был напуган Сталиным по причине: {reason}"))
        await asyncio.sleep(duration)
        await member.remove_roles(role)
        print(f"С пользователя {member.name} было снято заглушение")

    
def setup(client):
    client.add_cog(ModerCommands(client))