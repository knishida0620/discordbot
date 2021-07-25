#coding:utf-8
'''
DiscordのBOT用プログラム
'''
import json
import os
import discord
from discord.ext import commands
import random



client = discord.Client()


bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")


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

@client.event
async def on_message(message):
  print(message)
  #await client.delete_message(message)

