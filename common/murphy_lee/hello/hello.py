import nextcord
from nextcord.ext import commands

class MurphyHello(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
        self._last_member = None

  @nextcord.slash_command(name="hello0", description="Says hello!")
  async def hello(self, interaction: nextcord.Interaction, member: nextcord.Member = None):
      """Says hello"""
      member = member or interaction.user  # Use interaction.user instead of ctx.author
      if self._last_member is None or self._last_member.id != member.id:
          await interaction.response.send_message(f'Hello {member.name}~')  # Use interaction.response.send_message
      else:
          await interaction.response.send_message(f'Hello {member.name}... This feels familiar.')  # Use interaction.response.send_message
      self._last_member = member
