import discord
import os

client = discord.Client()

@client.event
async def on_ready():
     print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
      await message.channel.send('Twitter has a disincentive to reduce spam, as it reduces perceived daily users. It is suspicious')

client.run('PASTE_YOUR_BOT_TOKEN')
