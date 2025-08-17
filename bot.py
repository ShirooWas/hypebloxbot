import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

    # Ganti EMOJI_ID_VERIFY dengan ID emoji :verify:
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="over 10M+ IDR secure transactions <a:Reserved:1395938684867707061>"
    )

    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if content.startswith("+vouch robux"):
        await message.add_reaction("<:robux:EMOJI_ID_ROBUX>")
        await message.add_reaction("<:HypeBloxSociety:EMOJI_ID_HYPEBLOX>")

    elif content.startswith("+vouch limited"):
        await message.add_reaction("<:diamantee:EMOJI_ID_DIAMANTEE>")
        await message.add_reaction("<:HypeBloxSociety:EMOJI_ID_HYPEBLOX>")

client.run(TOKEN)
