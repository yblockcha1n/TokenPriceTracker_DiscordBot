import discord
from discord.ext import commands, tasks
import requests
import asyncio

TOKEN = "YOUR_BOT_TOKEN"

API_KEY = "CMC_API_KEY"

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = commands.Bot(command_prefix="/", intents=intents)

def format_price(price):
    if price < 0.01:
        return f"${price:.10f}" #価格が$0.01未満の場合、10桁まで表示 (草コイン対象)
    elif price < 1:
        return f"${price:.6f}" #$1未満の場合、6桁まで表示
    elif price < 10:
        return f"${price:.4f}" #$10未満の場合、4桁まで表示
    elif price < 100:
        return f"${price:.2f}" #$100未満の場合、2桁まで表示
    else:
        return f"${price:.0f}" #$100以上の場合、整数のみ表

# Botアクティビティ欄の価格表示
@tasks.loop(minutes=1)
async def update_coin_price():
    symbol = "COIN_SYMBOL" #任意のコインシンボルを大文字で指定 (ex. BTC)

    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}&CMC_PRO_API_KEY={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "data" in data and symbol in data["data"]:
        price = data["data"][symbol]["quote"]["USD"]["price"]
        formatted_price = format_price(price)
        activity = discord.Activity(type=discord.ActivityType.watching, name=formatted_price)
        await client.change_presence(activity=activity)
        
# /chartコマンドの価格送信
@client.command()
async def price(ctx):
    symbol = "COIN_SYMBOL" #任意のコインシンボルを大文字で指定 (ex. BTC)

    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}&CMC_PRO_API_KEY={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "data" in data and symbol in data["data"]:
        price = data["data"][symbol]["quote"]["USD"]["price"]
        formatted_price = format_price(price)
        await ctx.send(f"現在の$〇〇価格は{formatted_price}です。") #〇〇は任意

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    update_coin_price.start()

client.run(TOKEN)
