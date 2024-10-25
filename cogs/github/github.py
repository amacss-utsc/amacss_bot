import discord
from discord.ext import commands
from discord import app_commands
import aiohttp

class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Github cog is ready')

    @app_commands.command(name='pull-requests', description='Gets open pull requests from the GitHub repository')
    async def pull(self, interaction: discord.Interaction):
        """
        Fetches the number of open pull requests from the GitHub repository

        Note: Since we are using the Github API, unauthenticated requests are rate-limited to 60 per hour
        """
        await interaction.response.defer()
        url = 'https://api.github.com/repos/amacss-utsc/amacss_bot/pulls?state=open&per_page=30'
        total_pulls = 0

        async with aiohttp.ClientSession() as session:
            try:
                while url:
                    async with session.get(url) as response:
                        if response.status != 200:
                            await interaction.followup.send(f"Failed to fetch pull requests. Status code: {response.status}")
                            return

                        pulls = await response.json()
                        total_pulls += len(pulls)

                        # API Responds with max 30 pull requests per page so we must check if there are more pages
                        link_header = response.headers.get('Link')
                        url = self.get_next_page_url(link_header)

                await interaction.followup.send(f'Total open pull requests: {total_pulls}')

            except Exception as e:
                print(f"Error: {e}")
                await interaction.followup.send("An error occurred while fetching pull requests.")

    def get_next_page_url(self, link_header):
        """
        Parses the Link header to find the next page URL
        """
        if link_header:
            links = link_header.split(',')
            for link in links:
                if 'rel="next"' in link:
                    return link.split('<')[1].split('>')[0]
        return None

async def setup(bot):
    await bot.add_cog(Github(bot))
