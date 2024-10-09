import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from typing import Final
from cog_loader import cog_loader

async def main():
    # LOADING TOKEN
    load_dotenv()
    TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

    # BOT SETUP
    intents = discord.Intents.all()
    intents.message_content = True  # Enable the message content intent
    intents.members = True  # Enable the message content intent
    bot = commands.Bot(command_prefix="!", intents=intents)  # Set a command prefix

    # Event to show bot is ready
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')
    
    # Load cogs
    await cog_loader(bot)

    # Run the bot
    await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())