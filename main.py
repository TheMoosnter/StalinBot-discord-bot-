# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import datetime
import asyncio
from asyncio import sleep
import aiohttp
from discord import Webhook, AsyncWebhookAdapter

client = commands.Bot(command_prefix="~", intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print('[Система] Бот авторизован')
    print('------')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('тестирование бота'))

@client.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@client.command()
async def reg(ctx, *, arg, amount=1):
    await ctx.channel.purge(limit=amount)
    channel = client.get_channel(991769174286282762)
    await channel.send(arg)


client.run('ODE2Mzg4NzQwMjI1NDMzNjUy.Gplapb.FQK4xSxZ79IwOUrzJCuwdBqVuQ2EM-ozfQVhnM')