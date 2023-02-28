import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class SimpleView(discord.ui.View):

    @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("World")
        self.stop()

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelling")
        self.stop()


def run():
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
        response = {
            "content": "This is a message with components:", 
            "components": [
            {
                "type": 1,
                "components": []
            }
        ]}
        await ctx.send(response)

    @bot.command(name='button', help="we're testing buttons here")
    async def button(ctx):
        view = SimpleView()
        await ctx.send(view=view)
        


    bot.run(TOKEN, root_logger=True)

if __name__ == "__main__":
    run()