import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
from typing import Final
from cog_loader import cog_loader

def run_discord_bot() -> None:
    # LOADING TOKEN
    load_dotenv()
    TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

    # BOT SETUP
    bot = commands.Bot()
    cog_loader(bot)

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    # @bot.slash_command(description="My first slash command")
    # async def hello(interaction: nextcord.Interaction):
    #     await interaction.send("Hello!")

    bot.run(TOKEN)