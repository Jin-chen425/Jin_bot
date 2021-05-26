import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix= '[', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online<<")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(847052638688509962)
    await channel.send(f'{member} has arrived!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(847052667841675284)
    await channel.send(f'{member} has leaved!')
    
bot.run('ODQ3MDM2NDY0NTk1NDY4MzU4.YK4OLg.8x99bkh0ixZhv-y273FVpfy93D8')