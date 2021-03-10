import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event

#Prints a message to the command line when stripes is succesfully initated
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# These commands give Stripes a little personality
    #Stripes says hello when someone types $hello (good test command)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello! I don\'t know how to do a whole lot yet, but I\'m happy to be here! :)')

    #Stripes will react with the eyes emoji when his name is mentioned
    if 'stripes' in message.content or 'Stripes' in message.content:
        await message.add_reaction(u"\U0001F440")

#Get bot token from .env
client.run(os.getenv('TOKEN'))