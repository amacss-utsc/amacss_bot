from common.murphy_lee.hello.hello import MurphyHello
from exec.murphy_lee.channel_admin.channel_admin import MurphyChannelAdmin

# MUST ADD YOUR COGS HERE FOR YOUR COMMANDS TO WORK
def cog_loader(bot):
  bot.add_cog(MurphyHello(bot))
  bot.add_cog(MurphyChannelAdmin(bot))