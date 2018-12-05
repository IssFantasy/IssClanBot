import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='tagliarsi le vene'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!biscottodellafortuna':
        await client.send_message(message.channel,'oggi respirerai')
    if message.content == '!monster':
        await client.send_message(message.channel,'MoNsTeR MeRdA')
    if message.content == '!biscottodellafortuna2':
        await client.send_message(message.channel,'domani ti sveglierai')
    if message.content == '!monkas':
        em = discord.Embed(description='quando il truffatore ti truffa')
        em.set_image(url='https://cdn.discordapp.com/attachments/519157517100777473/519157818046021632/monka_s.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!perfection':
        em = discord.Embed(description='deja vous')
        em.set_image(url='https://cdn.discordapp.com/attachments/519159557264769038/519874117495685120/perfection.jpg')
    if message.content == '!younesmerda':
        em = discord.Embed(description='lol')
        em.set_image(url='https://cdn.discordapp.com/attachments/519159557264769038/519550047948636160/nm.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '!dio':
        em = discord.Embed(description='dio ti sta guardando')
        em.set_image(url='https://cdn.discordapp.com/attachments/519157517100777473/519160214893887488/jeez.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '!petriniascuola':
        await client.send_message(message.channel,'avrai sbagliato nome. Petrini non viene a scoula')
    if message.content == '!pd':
        em = discord.Embed(description='il pd ti guarda')
        em.set_image(url='https://cdn.discordapp.com/attachments/519157517100777473/519169473807253511/pd.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!beppe':
        em = discord.Embed(description='IL CACCIA DI BEPPE-MIKY')
        em.set_image(url='https://cdn.discordapp.com/attachments/519159557264769038/519873207864393736/caccia.png')
    if message.content == '!genio':
        em = discord.Embed(description='sei il nostro salvatore')
        em.set_image(url='https://cdn.discordapp.com/attachments/519159557264769038/519871636590034944/genius_nibba.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!bravissimo':
        em = discord.Embed(description='sei un genio')
        em.set_image(url='https://cdn.discordapp.com/attachments/519544327366770719/519812645835243530/you_dont_say.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!comandi':
        await client.send_message(message.channel,'perfection, beppe, dio, monster, bravissimo, genio, younesmerda, hacker, monkas, dio, biscottodellafortuna, petriniascuola, pd')
    if message.content == '!hacker':
        em = discord.Embed(description='quando riesci a trovare la password della scuola')
        em.set_image(url='https://cdn.discordapp.com/attachments/519157517100777473/519172372792606730/hacerman.jpg')
        await client.send_message(message.channel, embed=em)
client.run('NTE5MTUzMzcwNDIyODM3MjY5.DubQrg.ALKdq0sXFLR89j9vh1Y3s2zZfTk')
