from discord import Intents, Client, Message
import os
import responses
from dotenv import load_dotenv
from typing import Final


def run_discord_bot() -> None:
    # LOADING TOKEN
    load_dotenv()
    TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

    # BOT SETUP
    intents: Intents = Intents.default()
    intents.messages = True
    intents.message_content = True
    client: Client = Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username, user_message, channel = str(message.author), str(message.content), str(message.channel)

        print(f'{username} said "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, True)
        else:
            await send_message(message, user_message, False)

    client.run(TOKEN)

async def send_message(message: Message, user_message: str, is_private: bool) -> None:
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)