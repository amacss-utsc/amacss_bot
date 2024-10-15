import discord
from discord.ext import commands
from discord import app_commands
from models import session
from models.economy import EconomyPlayer, Inventory
import random

class Economy(commands.Cog):
    # FISH_TYPES maps a fish to (name, emoji, probability, selling_price)
    FISH_TYPES = {
        "fish": ("Fish", "🐟", 0.25, 10, "Common (1/4)"),
        "blowfish": ("Blowfish", "🐡", 0.2, 40, "Uncommon (1/5)"),
        "squid": ("Squid", "🦑", 0.15, 75, "Uncommon (1/6)"),
        "whale": ("Whale", "🐳", 0.11, 100, "Rare (1/9)"),
        "octopus": ("Octopus", "🐙", 0.09, 150, "Rare (1/11)"),
        "seal": ("Seal", "🦭", 0.08, 250, "Epic (1/12)"),
        "lobster": ("Lobster", "🦞", 0.06, 500, "Epic (1/17)"),
        "dolphin": ("Dolphin", "🐬", 0.05, 1000, "Legendary (1/20)"),
        "shark": ("Shark", "🦈", 0.01, 5000, "Legendary (1/50)")
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Economy cog is ready')

    @app_commands.command(name='inventory', description='View your inventory')
    async def inventory(self, interaction: discord.Interaction):
        try:
            player = session.query(EconomyPlayer).filter_by(discord_id=str(interaction.user.id)).first()

            if player is None:
                await interaction.response.send_message("You do not have an inventory.")
                return

            inventory = session.query(Inventory).filter_by(player_id=player.id).all()
            if not inventory:
                await interaction.response.send_message("You do not have any items in your inventory.")
                return
            
            inventory_with_rarity = [
                (self.FISH_TYPES[item.item_name][0], item.quantity, self.FISH_TYPES[item.item_name][1], self.FISH_TYPES[item.item_name][2], self.FISH_TYPES[item.item_name][3], self.FISH_TYPES[item.item_name][4])
                for item in inventory if item.item_name in self.FISH_TYPES
            ]

            sorted_inventory = sorted(inventory_with_rarity, key=lambda x: x[3], reverse=True)

            embed = discord.Embed(
                title=f"{interaction.user.name}'s Inventory",
                description=f"💰 **Coins**: {player.balance}\n",
                timestamp=discord.utils.utcnow()
            )

            embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)

            for item_name, quantity, emoji, _, price, rarity in sorted_inventory:
                embed.add_field(
                    name=f"{emoji} {item_name} (x{quantity})",
                    value=f"Rarity: {rarity}\nSell Price: {price} coins",
                    inline=True
                )
            
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)
            await interaction.response.send_message(f"An error occurred.")

    @app_commands.command(name='fish', description='Put your rod in and see what happens!')
    async def fish(self, interaction: discord.Interaction):
        try:
            item_type = "FISHING_ITEM"

            fish_types = list(self.FISH_TYPES.keys())
            fish_weights = [weight for _, _, weight, _, _ in self.FISH_TYPES.values()]
            caught_fish = random.choices(fish_types, weights=fish_weights)[0]
            caught_fish_name, caught_fish_emoji, _, _, _ = self.FISH_TYPES[caught_fish]

            player = session.query(EconomyPlayer).filter_by(discord_id=str(interaction.user.id)).first()

            if player is None:
                player = EconomyPlayer(discord_id=str(interaction.user.id), discord_name=interaction.user.name)
                session.add(player)
                session.commit()

            inventory_item = session.query(Inventory).filter_by(player_id=player.id, item_name=caught_fish).first()
            if inventory_item:
                inventory_item.quantity += 1
            else:
                inventory_item = Inventory(player_id=player.id, item_name=caught_fish, item_type=item_type, quantity=1)
                session.add(inventory_item)
            
            session.commit()

            await interaction.response.send_message(f"{caught_fish_emoji} {interaction.user.mention}, You caught a {caught_fish_name}!")
        except Exception as e:
            print(e)
            await interaction.response.send_message(f"An error occurred.")

    @app_commands.command(name="sell", description="Sell an item from your inventory")
    async def sell(self, interaction: discord.Interaction, item_name: str, quantity: int):
        try:
            item_name = item_name.lower()
            player = session.query(EconomyPlayer).filter_by(discord_id=str(interaction.user.id)).first()

            if player is None:
                await interaction.response.send_message("You don't have an account yet!")
                return

            inventory_item = session.query(Inventory).filter_by(player_id=player.id, item_name=item_name).first()

            if inventory_item is None:
                await interaction.response.send_message(f"You don't have any {item_name} in your inventory.")
                return

            if inventory_item.quantity < quantity:
                await interaction.response.send_message(f"You don't have enough {item_name} to sell. You only have {inventory_item.quantity}.")
                return

            if item_name not in self.FISH_TYPES:
                await interaction.response.send_message(f"{item_name} is not a valid item to sell.")
                return

            _, _, _, price, _ = self.FISH_TYPES[item_name]
            total_sale_value = price * quantity

            # Update inventory
            inventory_item.quantity -= quantity
            if inventory_item.quantity == 0:
                session.delete(inventory_item)

            # Update player balance
            player.balance += total_sale_value

            session.commit()

            await interaction.response.send_message(f"You sold {quantity} {item_name} for {total_sale_value} coins! 💰 You now have {player.balance} coins.")
        except Exception as e:
            print(e)
            await interaction.response.send_message("An error occurred while processing your sale.")

async def setup(bot):
    await bot.add_cog(Economy(bot))