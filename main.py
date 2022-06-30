# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
# import datetime
# import asyncio
# from asyncio import sleep
# import aiohttp
# from discord import Webhook, AsyncWebhookAdapter
import os

client = commands.Bot(command_prefix="~", intents=discord.Intents.all())
client.remove_command('help')


@client.event
async def on_ready():
    print('[Система] Бот авторизован')
    print('------')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('тестирование бота'))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Игрок')  # САМА РОЛЬ КОТОРУЮ ВЫДАЕМ
    await member.add_roles(role)  # ДОБАВЛЯЕМ РОЛЬ
    print(f"Пользователю {member.name} была выдана роль игрок.")

@client.command()
async def reg(ctx, *, arg, amount = 1):
    await ctx.channel.purge(limit=amount)
    channel = client.get_channel(991769174286282762)
    await channel.send(arg)

'''@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            embed=discord.Embed(title='[ARG_ERROR]', description='Недостаточно аргументов для выполнения этой команды.',
                                colour=discord.Colour.red()))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            embed=discord.Embed(title='[PERMS_ERROR]', description='Недостаточно прав для выполнения этой команды.',
                                colour=discord.Colour.red()))
    if isinstance(error, commands.MemberNotFound):
        await ctx.send(
            embed=discord.Embed(title='[MEMBER_ERROR]', description='Участник не найден.', colour=discord.Colour.red()))'''


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 563270997067825153 or 864557971350093847:
        client.load_extension(f"cogs.{extension}")
        await ctx.send("Коги загружены")
    else:
        await ctx.send("Вы не разработчик бота")


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 563270997067825153 or 864557971350093847:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send("Коги загружены")
    else:
        await ctx.send("Вы не разработчик бота")


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 563270997067825153 or 864557971350093847:
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")
        await ctx.send("Коги загружены")
    else:
        await ctx.send("Вы не разработчик бота")


@client.group(invoke_without_command=True)
async def help(ctx):
    # if On == 'True':
    emb = discord.Embed(title='Мои команды:',
                        colour=discord.Colour.green())

    emb.add_field(name='Обычные команды', value='Класические команды. Подробнее: !~help SimpleCommands')
    emb.add_field(name='Команды для модерирования', value='Команды модерации. Подробнее: !~help ModerCommands')
    emb.add_field(name='Текстовые команды',
                  value='Команды для работы с текстом. В основном идёт использование webhooks. Подробнее: !~help TextCommands')
    #emb.add_field(name='~VoiceCommands ALPHA',
    #              value='Команды с использованием голосового канала. Подробнее: !~help VoiceCommands')
    # emb.add_url( url = 'https://google.com' )
    # emb.set_footer( text = 'Дискорд сервер бота: https://discord.com/invite/z3u53MF3jD')

    await ctx.send(embed=emb)


@help.command()
async def SimpleCommands(ctx):
    emb = discord.Embed(title='Группа "Обычные команды":', colour=discord.Colour.green())

    #emb.add_field(name='!~say', value='Сказать что-то от лица бота. Использование: !~say любой текст')
    emb.add_field(name='!~clear',
                  value='Очистить указаное кол-во сообщений. Если не указать число то будет удалено 100 сообщений. Использование: !~clear 50')
    emb.add_field(name='!~avatar', value='Показать аватар упомянутого участника. Использование: !~avatar @участник')

    await ctx.send(embed=emb)


@help.command()
async def TextCommands(ctx):
    emb = discord.Embed(title='Группа "Текстовые команды":', description='**ВНИМАНИЕ!!! ВСЕ КОМАНДЫ МОЖНО ИСПОЛЬЗОВАТЬ ТОЛЬКО УЧАСТНИКАМ С ПРАВАМИ АДМИНИСТРАТОРА', colour=discord.Colour.green())

    emb.add_field(name='!~serverEmbed',
                  value='Оформление embed-сообщения от лица сервера. Использование: !~serverEmbed "Заглавие" "Описание" (всё с кавычками)')
    emb.add_field(name='!~botEmbed',
                  value='Оформление embed-сообщения от лица бота. Использование: !~botEmbed "Заглавие" "Описание" (всё с кавычками)')
    emb.add_field(name='!~userEmbed',
                  value='Оформление embed-сообщения от вашего лица. Использование: !~userEmbed "Заглавие" "Описание" (всё с кавычками)')
    await ctx.send(embed=emb)


@help.command()
async def VoiceCommands(ctx):
    emb = discord.Embed(title='Команды группы VoiceCommands:',
                        description='**ВНИМАНИЕ!! Данная группа команд на данный момент находится на альфа тестировании. Некоторые функции могут работать неккоретно.**',
                        colour=discord.Colour.green())

    emb.add_field(name='!~youtube',
                  value='Открывает приложение Youtube в голосовом канале. Для использования зайдите в голосовой канал. Использование: !~youtube. После этого вам отправится ссылка. Нажмите на неё и всё готово. ')
    emb.add_field(name='!~chess',
                  value='Открывает приложение Chess In The Park в голосовом канале. Для использования зайдите в голосовой канал. Использование: !~youtube. После этого вам отправится ссылка. Нажмите на неё и всё готово.')
    await ctx.send(embed=emb)


@help.command()
async def ModerCommands(ctx):
    emb = discord.Embed(title='Команды группы ModerCommands:', colour=discord.Colour.green())

    emb.add_field(name='!~kick', value='Удаляет пользователя с дискорд сервера. Использование: !~kick @участник ')
    emb.add_field(name='!~ban', value='Банит упомянутого пользователя навсегда. Использование: !~ban @участник')
    emb.add_field(name='!~tempban',
                  value='Банит на время упомянутого пользователя. Указаное число идёт в секундах. Использование: !~tempban 10 @участник "причина" (с кавычками)')
    emb.add_field(name='!~unban', value='Разбан упомянутого пользователя. Использование: !~unban @участник')
    await ctx.send(embed=emb)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run('ODE2Mzg4NzQwMjI1NDMzNjUy.Gplapb.FQK4xSxZ79IwOUrzJCuwdBqVuQ2EM-ozfQVhnM')