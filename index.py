# coding:utf-8
'''
DiscordのBOT用プログラム
'''
import json
import os
import discord
from discord.ext import commands
import random

from discord.ext.commands.errors import NoEntryPointError
import modules.omikuji

configFile = None  # BOT設定
bot=None
client =None

def loadConfig():
    '''
    設定読み込み
    '''
    global configFile

    f = open('json/config.json', encoding='utf8')
    configFile = json.load(f)

print("設定読み込み")    
loadConfig()
print("初期化["+configFile["PREFIX"]+"]")
client = discord.Client()

bot = commands.Bot(command_prefix="!")
#bot = commands.Bot(command_prefix=configFile["PREFIX"])
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

@bot.event
async def on_message(message):
  #print(message)
  pass

@bot.event
async def test(ctx):
    await ctx.send("test.okゆうたです")


@bot.event
async def test2(ctx):
    await ctx.send("さそりのゆうたです")


@bot.event
async def おみくじ(ctx):
    omikuji = configFile["OMIKUJI"]
    result = random.choice(omikuji)
    await ctx.send("今日の運勢は" + result + "です！")


@bot.event
#@commands.has_role("admin")
async def ぱーじ(ctx,target:int):
  channel = ctx.message.channel
  print("★★"+str(target))
  deleted = await channel.purge(limit=target)
  await ctx.send(f"{len(deleted)}メッセージを削除しました")

###サーバー入室メッセージ
@bot.event
async def on_member_join(member):
    print("★★メンバ参加")
    serverID = 828090579928875009
    channelID=828104886116941825
    guild = bot.get_guild(serverID)
    channel = guild.get_channel(channelID)
    await channel.send(f"{member.name}が入室しました。楽しんで！！")

if __name__ == '__main__':
    '''
    '''

    bot.run(configFile["TOKEN"])
