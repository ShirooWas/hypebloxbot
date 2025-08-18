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
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="over 10M+ IDR secure transactions"
    )
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if content.startswith("+vouch robux"):
        robux_emoji = discord.utils.get(message.guild.emojis, name="robux")
        hypeblox_emoji = discord.utils.get(message.guild.emojis, name="HypeBloxSociety")

        if robux_emoji:
            await message.add_reaction(robux_emoji)
        if hypeblox_emoji:
            await message.add_reaction(hypeblox_emoji)

    elif content.startswith("+vouch limited"):
        diamantee_emoji = discord.utils.get(message.guild.emojis, name="diamantee")
        hypeblox_emoji = discord.utils.get(message.guild.emojis, name="HypeBloxSociety")

        if diamantee_emoji:
            await message.add_reaction(diamantee_emoji)
        if hypeblox_emoji:
            await message.add_reaction(hypeblox_emoji)

client.run(TOKEN)

