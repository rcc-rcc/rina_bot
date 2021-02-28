import discord
from discord.ext import commands
import asyncio
import os
import subprocess
import ffmpeg
from voice_generator import creat_WAV
import time
import random
import datetime

bot = commands.Bot(command_prefix='Rb.')
voice_bot = None


@bot.event
async def on_ready():
    print("------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')






@bot.command()
async def おいで(ctx):
    print('#join')
    print('#voicechannelを取得')
    vc = ctx.author.voice.channel
    print('#voicechannelに接続')
    await vc.connect()

@bot.command()
async def ばいばい(ctx):
    print('#bye')
    print('#切断')
    await ctx.voice_client.disconnect()

@bot.command()
async def register(ctx, arg1, arg2):
    with open('C:/open_jtalk/bin/dic.txt', mode='a') as f:
        f.write('\n'+ arg1 + ',' + arg2)
        print('dic.txtに書き込み：''\n'+ arg1 + ',' + arg2)
    await ctx.send('`' + arg1+'` を `'+arg2+'` として登録しました')

@bot.event
async def on_voice_state_update(member, before, after):
    server_id_test = "サーバーID"
    text_id_test = "通知させたいテキストチャンネルID"


    if member.guild.id == server_id_test:   # サーバーid
        text_ch = bot.get_channel(text_id_test)   # 通知させたいTEXTチャンネルid
        if before.channel is None:
            msg = f'【VC参加ログ】{member.name} が {after.channel.name} に参加しました。'
            await text_ch.send(msg)

@bot.event
async def on_message(message):
    print('---on_message_start---')
    msgbot = message.guild.voice_client
    print(msgbot)
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            print('#message.content:'+ message.content)
            creat_WAV(message.author.name + message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass
    await bot.process_commands(message)
    print('---on_message_end---')

@bot.command()
async def pien(ctx):
    print('#join')
    
    vc = ctx.author.voice.channel
    
    await vc.connect()
    source = discord.FFmpegPCMAudio("pien.mp3")
    ctx.guild.voice_client.play(source)
   


bot.run("DISCORD_BOT_TOKEN")

