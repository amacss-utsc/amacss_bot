import nextcord
from nextcord.ext import commands

class MurphyHello(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
        self._last_member = None

  @nextcord.slash_command(name="hello", description="Says hello!")
  async def hello(self, ctx, *, member: nextcord.Member = None):
      """Says hello"""
      member = member or ctx.author
      if self._last_member is None or self._last_member.id != member.id:
          await ctx.send(f'Hello {member.name}~')
      else:
          await ctx.send(f'Hello {member.name}... This feels familiar.')
      self._last_member = member