import csv
import io
import nextcord
from nextcord.ext import commands

class MurphyChannelAdmin(commands.Cog):
  def __init__(self, bot):
        self.bot = bot

  @nextcord.slash_command(name="create_channels_csv", description="Creates channels based on a CSV file!")
  @commands.has_permissions(manage_channels=True, manage_roles=True)
  async def create_channels_csv(self, interaction: nextcord.Interaction, attachment: nextcord.Attachment = None):
    await interaction.response.defer()
    
    # Check if there is an attachment
    if not attachment:
        await interaction.followup.send("Please provide a CSV file as an attachment.")
        return

    # Check if the attachment is a CSV file
    if not attachment.filename.endswith('.csv'):
        await interaction.followup.send("The attachment must be a CSV file.")
        return

    # Read the CSV file from the attachment
    attachment_bytes = await attachment.read()
    csv_file = io.StringIO(attachment_bytes.decode('utf-8'))
    reader = csv.reader(csv_file)

    # Create channels based on the first column of each row
    for i, row in enumerate(reader):
        if i == 0:
            continue
        channel_name = row[0]
        is_private = row[1].lower() == "yes"
        roles = row[2].split(';') if row[2] else []
        category_name = row[3]
        try:
            # Check if category exists
            category = nextcord.utils.get(interaction.guild.categories, name=category_name)
            if not category:
                await interaction.followup.send(f"Error: Category '{category_name}' not found.")
                return

            # Check if roles exist
            role_objects = []
            for role_name in roles:
                role = nextcord.utils.get(interaction.guild.roles, name=role_name)
                if not role:
                    await interaction.followup.send(f"Error: Role '{role_name}' not found.")
                    return
                role_objects.append(role)

            # Create the channel
            overwrites = {role: nextcord.PermissionOverwrite(read_messages=True) for role in role_objects} if is_private else None
            if is_private:
                overwrites[interaction.guild.default_role] = nextcord.PermissionOverwrite(read_messages=False)
            await interaction.guild.create_text_channel(name=channel_name, category=category, overwrites=overwrites)
        except Exception as e:
            await interaction.followup.send(f"Error creating channel '{channel_name}': {e}")
    await interaction.followup.send("Channel creation completed.")
      
  @nextcord.slash_command(name="create_role", description="Create a new role with the given name")
  @commands.has_permissions(manage_roles=True)
  async def create_role(self, interaction: nextcord.Interaction, role_name: str):
      # Check if the role already exists
      existing_role = nextcord.utils.get(interaction.guild.roles, name=role_name)
      if existing_role:
          await interaction.response.send_message(f"A role named '{role_name}' already exists.")
          return

      try:
          # Create the role
          await interaction.guild.create_role(name=role_name)
          await interaction.response.send_message(f"Role '{role_name}' created successfully.")
      except Exception as e:
          await interaction.followup.send(f"Error creating role: {e}")

  @nextcord.slash_command(name="create_roles_from_file", description="Create roles from a TXT file")
  @commands.has_permissions(manage_roles=True)
  async def create_roles_from_file(self, interaction: nextcord.Interaction, attachment: nextcord.Attachment = None):
      await interaction.response.defer()

      if not (attachment or attachment.filename.endswith('.txt')):
          await interaction.followup.send("Please provide a TXT file.")
          return
      
      attachment_bytes = await attachment.read()
      file_content = io.StringIO(attachment_bytes.decode('utf-8'))
      role_names = file_content.read().splitlines()

      for role_name in role_names:
          role_name = role_name.strip()
          existing_role = nextcord.utils.get(interaction.guild.roles, name=role_name)
          if existing_role:
              await interaction.followup.send(f"Role '{role_name}' already exists.")
              continue

          try:
              await interaction.guild.create_role(name=role_name)
              await interaction.followup.send(f"Role '{role_name}' created successfully.")
          except Exception as e:
              await interaction.followup.send(f"Error creating role '{role_name}': {e}")