import discord
import os
from dotenv import load_dotenv

# Load environment variables dari .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if content.startswith("+vouch robux"):
        try:
            await message.add_reaction("<:robux:1406669479898775663>")
            await message.add_reaction("<:HypeBloxSociety:1406659611909423296>")
        except Exception as e:
            print(f"Gagal react robux: {e}")

    elif content.startswith("+vouch limited"):
        try:
            await message.add_reaction("<:diamantee:1406669782484385812>")
            await message.add_reaction("<:HypeBloxSociety:1406659611909423296>")
        except Exception as e:
            print(f"Gagal react limited: {e}")

client.run(TOKEN)
