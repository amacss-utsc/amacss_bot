import nextcord
from nextcord.ext import commands

class MurphyChannelAdmin(commands.Cog):
  def __init__(self, bot):
        self.bot = bot

  @nextcord.slash_command(name="create_channels_csv", description="Says hello!")
  @commands.has_permissions(manage_channels=True, manage_roles=True)
  async def create_channels_csv(self, ctx):
      pass
      