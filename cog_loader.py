import os

# MUST ADD YOUR COGS HERE FOR YOUR COMMANDS TO WORK
async def cog_loader(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
