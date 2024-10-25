import discord
from discord.ext import commands
from discord import app_commands
import random
import os

class Gifs(commands.Cog):
    LIE_GIF = "https://tenor.com/view/lie-lie-detector-cap-you-are-lying-stop-lying-gif-12198388917433403789"
    TRUTH_GIF = "https://tenor.com/view/lie-detector-meme-truth-lie-gif-9021535758661504197"
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Gifs cog is ready')

    @app_commands.command(name='lie', description='If they capping CALL EM OUT 🗣️')
    async def lie(self, interaction: discord.Interaction):
        await interaction.response.send_message(self.LIE_GIF)

    @app_commands.command(name='truth-or-lie', description='The ultimate test of honesty')
    @app_commands.describe(prompt="Ask a question to test the truth!")
    async def truth_or_lie(self, interaction: discord.Interaction, prompt: str):
        response_gif = self.TRUTH_GIF if random.choice([True, False]) else self.LIE_GIF
        await interaction.response.send_message(f'**"{prompt}":**')
        await interaction.followup.send(response_gif)

    @app_commands.command(name='sad', description='When it has been a long day')
    async def sad(self, interaction: discord.Interaction):
        try:
            # load sad gifs from the text file
            file_path = os.path.join(os.path.dirname(__file__), 'sad.txt')
            with open(file_path, 'r') as file:
                sad_gifs = file.readlines()
            
            # strip newline characters + choose random sad gif
            random_sad_gif = random.choice([gif.strip() for gif in sad_gifs])
            await interaction.response.send_message(random_sad_gif)
        except FileNotFoundError:
            # Sad gif file not found :OO
            await interaction.response.send_message("Try again later ¯\\_(ツ)_/¯")
        


async def setup(bot):
    await bot.add_cog(Gifs(bot))