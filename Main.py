import discord
from discord.ext import commands
import random
import os
from Model import get_class
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Привет! Я бот {bot.user}!")

@bot.command()
async def bye(ctx):
    await ctx.send(f"Bye!")


@bot.command()
async def mem(ctx):
    random_list = os.listdir('images')
    rand_mem = random_list
    with open(f'images/{rand_mem}', 'rb') as f:           
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_URL = attachment.url
            await attachment.save(f"images/{file_name}")
            await ctx.send(get_class(model="keras_model.1h5", labels="labels1.txt", image=f"images/{file_name}"))
    else:
        await ctx.send("Вы забыли картинку")

@bot.command()
async def eco(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_URL = attachment.url
            await attachment.save(f"images/{file_name}")
            await ctx.send(get_class(model="keras_model_2.h5", labels="labels_2.txt", image=f"images/{file_name}"))
bot.run("MTE0OTczNjY5NjUxMDk0MzM2Mw.GGzurz.iJC10HVAdhwHbf82f6Tof4NYdzxE0uR72fQvLo") 