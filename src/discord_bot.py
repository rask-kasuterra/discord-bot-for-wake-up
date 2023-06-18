import os
import requests
import discord

from discord import app_commands
from dotenv import load_dotenv

load_dotenv('configs/.env')

API_KEY = os.getenv('API_KEY')
API_GATEWAY_ENDPOINT = os.getenv('API_GATEWAY_ENDPOINT')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="start_mc", description="Start Minecraft EC2 Instance")
async def start(interaction: discord.Interaction):
    headers = {'Content-Type': 'application/json', 'x-api-key': API_KEY}

    print(f"end_point: {API_GATEWAY_ENDPOINT}/start")
    response = requests.post(f"{API_GATEWAY_ENDPOINT}/start", headers=headers)

    await interaction.response.send_message("マイクラサーバ起動中",ephemeral=False)

@tree.command(name="stop_mc", description="Stop Minecraft EC2 Instance")
async def stop(interaction: discord.Interaction):
    headers = {'Content-Type': 'application/json', 'x-api-key': API_KEY}

    print(f"end_point: {API_GATEWAY_ENDPOINT}/stop")
    response = requests.post(f"{API_GATEWAY_ENDPOINT}/stop", headers=headers)
    await interaction.response.send_message("マイクラサーバ停止中",ephemeral=False)

@client.event
async def on_ready():
    await tree.sync()#スラッシュコマンドを同期
    print("起動完了")

client.run(DISCORD_TOKEN)
