import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import os
import aiohttp

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"bot connected as {bot.user.name}")

@bot.command()
async def BrookhavenPlayers(ctx):
    url = "https://www.roblox.com/games/4924922222/Brookhaven-RP"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Brookhaven is: {players_count}")


@bot.command()
async def TSBPlayers(ctx):
    url = "https://www.roblox.com/games/10449761463/The-Strongest-Battlegrounds"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing The Strongest Battlegrounds is: {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def playersMM2(ctx):
    url = "https://www.roblox.com/games/142823291/Murder-Mystery-2"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, 'html.parser')
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Murder Mystery 2 is: {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def royalehighPlayers(ctx):
    url = "https://www.roblox.com/games/735030788/Royale-High#ropro-quick-search"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Royale High is: {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def BloxFruitsPlayers(ctx):
    url = "https://www.roblox.com/games/2753915549/Blox-Fruits"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Blox Fruits is: {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def rules(ctx):
    await ctx.reply(f"1. Do not spam on the chat 2. Do not send memes")

@bot.command()
async def commands(ctx):
    await ctx.reply(f"!rules !playersMM2 !royalehighPlayers")


bot.run("MTExODMxMzAyMzkyMTE5Mjk2MQ.GGE1T9.bi8d9BgRiRvpTbv-yqwQUM7OyyRmQq_kbyQBAE")
