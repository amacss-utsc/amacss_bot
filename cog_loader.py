from common.murphy_lee.hello.hello import MurphyHello

# MUST ADD YOUR COGS HERE FOR YOUR COMMANDS TO WORK
def cog_loader(bot):
  bot.add_cog(MurphyHello(bot))