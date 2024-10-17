import discord
from discord.ext import commands
from discord import app_commands
import random

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

    # Non-slash command, which lets you reply to a message with the lie GIF (slash commands can't be used as replies)
    @commands.command(name='lie', help='If they capping CALL EM OUT 🗣️')
    async def lie(self, ctx):
        if ctx.message.reference:
            original_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            await original_message.reply(self.LIE_GIF, mention_author=True)
        else:
            await ctx.send(self.LIE_GIF)

    @app_commands.command(name='truth-or-lie', description='The ultimate test of honesty')
    @app_commands.describe(prompt="Ask a question to test the truth!")
    async def truth_or_lie(self, interaction: discord.Interaction, prompt: str):
        response_gif = self.TRUTH_GIF if random.choice([True, False]) else self.LIE_GIF
        await interaction.response.send_message(f'**"{prompt}":**')
        await interaction.followup.send(response_gif)

async def setup(bot):
    await bot.add_cog(Gifs(bot))