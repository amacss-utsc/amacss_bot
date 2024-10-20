import discord
from discord.ext import commands
from discord import app_commands
import random

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping cog is ready')

    @app_commands.command(name='ping', description='Ping the bot')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    @app_commands.command(name='affirm', description='Get a positive affirmation')
    async def affirm(self, interaction: discord.Interaction):
        # Load affirmations from the text file
        try:
            with open('affirmations.txt', 'r') as file:
                affirmations = file.readlines()
            # Strip newline characters + choose random affirmation
            random_affirmation = random.choice([affirmation.strip() for affirmation in affirmations])
            await interaction.response.send_message(random_affirmation)
        except FileNotFoundError:
            # Affirmation file not found :OO
            await interaction.response.send_message("Try again later ¯\_(ツ)_/¯")


async def setup(bot):
    await bot.add_cog(Ping(bot))