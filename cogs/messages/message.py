# cogs/generic/ping.py
import discord
from discord.ext import commands
from discord import app_commands
import random
import os

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Message cog is ready')

    @app_commands.command(name='affirm', description='Get a positive affirmation')
    async def affirm(self, interaction: discord.Interaction):
        # Load affirmations from the text file
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'affirmations.txt')
            with open(file_path, 'r') as file:
                affirmations = file.readlines()
            # Strip newline characters + choose random affirmation
            random_affirmation = random.choice([affirmation.strip() for affirmation in affirmations])
            await interaction.response.send_message(random_affirmation)
        except FileNotFoundError:
            # Affirmation file not found :OO
            await interaction.response.send_message("Try again later ¯\\_(ツ)_/¯")

  
async def setup(bot):
    await bot.add_cog(Message(bot))