import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents(messages=True, guilds=True)
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents = intents)

@bot.command(name='hi', help='prints hello world to greet you')
async def hello_world(ctx):
    response = "Hello World"
    await ctx.send(response)

@bot.command(name='ask-pronouns', help='will ask user to click their pronouns and will add this to their nickname')
async def ask_pronouns(ctx):
    response = {"content": "This is a message with components:", "components": [
        {
            "type": 1,
            "components": []
        }
    ]}
    await ctx.send(response)
bot.run(TOKEN)



# client = discord.Client(intents = intents)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if message.content.startswith('>hi'):
#         await message.channel.send('Hello World!')

#     elif message.content.startswith('>ask-pronouns'):
#         await message.channel.send('Initiating pronoun asking sequence.')

# client.run(TOKEN)