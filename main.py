# 

import discord
import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} sent "{user_message}" in {channel}')

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if ("เพิ่มงาน" in user_message)and( "ผู้ช่วยคุง" in user_message):
        await message.channel.send('www')
    
    if ("checkfield" in user_message.lower):
        await message.channel.send('www')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'Welcome to the server, {member.mention}!')

todolist = discord.Embed(
    title = "รายการงานปัจจุบัน",
    description = "งานค้างทั้งหลาย",
    color = 0x40FF00 
)


client.run('')