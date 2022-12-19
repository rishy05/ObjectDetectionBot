from discord.ext import commands
import discord
import uuid
import requests
import shutil
from detect import parse_opt, main
from PIL import Image as img
import os

client = commands.Bot(command_prefix = ['O '], intents = discord.Intents.all())

opt = parse_opt()

@client.event
async def on_ready():
    print("Ready")

@client.command()
async def detect(ctx):
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("No fille attached")
        await ctx.channel.send("No file attached")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            imgName = str(uuid.uuid4()) + '.jpg'
            with open(imgName, 'wb') as out_file:
                print(f"File saved as {imgName}") 
                shutil.copyfileobj(r.raw, out_file)
            shutil.move(f'E:\obj_discord\content\yolov5\{imgName}', "E:\obj_discord\content\yolov5\data\imgss")
            main(opt)
            with open(f'E:\obj_discord\content\yolov5\data\send_data\exp\{imgName}', 'rb') as f:
                picture = discord.File(f)
                await ctx.channel.send(file = picture)
            os.remove(f"E:\obj_discord\content\yolov5\data\imgss\{imgName}")
            shutil.rmtree('E:\obj_discord\content\yolov5\data\send_data\exp')


@client.command()
async def obj(ctx):
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("No fille attached")
        await ctx.channel.send("No file attached")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            vidName = str(uuid.uuid4()) + '.mp4'
            with open(vidName, 'wb') as out_file:
                print(f"File saved as {vidName}") 
                shutil.copyfileobj(r.raw, out_file)
            shutil.move(f'E:\obj_discord\content\yolov5\{vidName}', "E:\obj_discord\content\yolov5\data\imgss")
            main(opt)
            with open(f'E:\obj_discord\content\yolov5\data\send_data\exp\{vidName}', 'rb') as f:
                video = discord.File(f)
                await ctx.channel.send(file = video)
            os.remove(f"E:\obj_discord\content\yolov5\data\imgss\{vidName}")
            shutil.rmtree('E:\obj_discord\content\yolov5\data\send_data\exp')



client.run("API KEY")
