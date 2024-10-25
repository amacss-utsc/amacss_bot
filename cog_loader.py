import os
import asyncio

async def cog_loader(bot):
    # MUST ADD YOUR COGS HERE FOR YOUR COMMANDS TO WORK
    cogs = [
        "cogs.generic.ping",
        "cogs.games.economy",
        "cogs.memes.gifs",
        "cogs.github.github",
        "cogs.messages.message"
    ]
    load_tasks = [bot.load_extension(cog) for cog in cogs]
    
    await asyncio.gather(*load_tasks)
