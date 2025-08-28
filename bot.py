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
        name="over 150M+ IDR secure transactions"
    )
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    # VOUCH ROBUX
    if content.startswith("+vouch robux"):
        robux_emoji = discord.utils.get(message.guild.emojis, name="robux")
        hypeblox_emoji = discord.utils.get(message.guild.emojis, name="HypeBloxSociety")

        if robux_emoji:
            await message.add_reaction(robux_emoji)
        if hypeblox_emoji:
            await message.add_reaction(hypeblox_emoji)

    # VOUCH LIMITED
    elif content.startswith("+vouch limited"):
        diamantee_emoji = discord.utils.get(message.guild.emojis, name="diamantee")
        hypeblox_emoji = discord.utils.get(message.guild.emojis, name="HypeBloxSociety")

        if diamantee_emoji:
            await message.add_reaction(diamantee_emoji)
        if hypeblox_emoji:
            await message.add_reaction(hypeblox_emoji)

    # PAYMENT METHOD
    elif content.startswith("!payment"):
        embed = discord.Embed(
            title="💳 METODE PEMBAYARAN",
            description=(
                "**BCA** `8335304175` (KHUSUS ROBUX)\n"
                "**BRI** `453701010461506` (KHUSUS LIMITED ITEM)"
            ),
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)

    # PRICELIST ROBUX VIA GAMEPASS
    elif content.startswith("!pricelist robux via gamepass"):
        robux_emoji = discord.utils.get(message.guild.emojis, name="robux")
        emoji_str = str(robux_emoji) if robux_emoji else "💰"
        small_image_url = "https://media.discordapp.net/attachments/1396302458602655814/1406487770041548880/HpyeBlox_Society.png?format=webp&quality=lossless&width=943&height=943"

        # BEFORE TAX
        embed_before = discord.Embed(
            title="💸 PRICE LIST ROBUX VIA GAMEPASS",
            color=discord.Color.yellow()
        )
        embed_before.set_thumbnail(url=small_image_url)
        embed_before.add_field(
            name="📌 VIA GAMEPASS (BEFORE TAX 30%)",
            value=(
                "**5 DAYS = 120 HOURS**\n"
                "100% Clean, Guaranteed Anti CC/Phising\n\n"
                f"{emoji_str} 100  = Rp 9.000\n"
                f"{emoji_str} 500  = Rp 45.000\n"
                f"{emoji_str} 1.000 = Rp 90.000\n"
                f"{emoji_str} 5.000 = Rp 450.000\n"
                f"{emoji_str} 10.000 = Rp 900.000\n\n"
                f"*Note: Tersedia dari {emoji_str}100 hingga seterusnya sesuai request.*"
            ),
            inline=False
        )

        # AFTER TAX
        embed_after = discord.Embed(
            title="💸 PRICE LIST ROBUX VIA GAMEPASS",
            color=discord.Color.yellow()
        )
        embed_after.set_thumbnail(url=small_image_url)
        embed_after.add_field(
            name="📌 VIA GAMEPASS (AFTER TAX 30%)",
            value=(
                "**5 DAYS = 120 HOURS**\n"
                "100% Clean, Guaranteed Anti CC/Phising\n\n"
                f"{emoji_str} 100  = Rp 13.000\n"
                f"{emoji_str} 500  = Rp 65.000\n"
                f"{emoji_str} 1.000 = Rp 130.000\n"
                f"{emoji_str} 5.000 = Rp 650.000\n"
                f"{emoji_str} 10.000 = ~~Rp 1.300.000~~ Rp 1.250.000\n\n"
                f"*Note: Tersedia dari {emoji_str}100 hingga seterusnya sesuai request.*"
            ),
            inline=False
        )

        await message.channel.send(embed=embed_before)
        await message.channel.send(embed=embed_after)

    # INFO GAMEPASS (BEFORE & AFTER TAX)
    elif content.startswith("!gamepass"):
        embed = discord.Embed(
            title="📖 Informasi Gamepass Robux",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="1. Before Tax (sebelum pajak)",
            value=(
                "Pembelian jumlah awal Robux sebelum dipotong pajak oleh Roblox 30%.\n\n"
                "```Contoh: misalnya kamu beli 1000 Robux maka masuk nya hanya 700 Robux "
                "karena dipotong 30% oleh Roblox (tidak full).```"
            ),
            inline=False
        )

        embed.add_field(
            name="2. After Tax (setelah pajak)",
            value=(
                "Pembelian jumlah Robux sesudah dipotong pajak oleh Roblox.\n\n"
                "```Contoh: misalnya kamu beli 1000 Robux maka masuk nya akan 1000 Robux juga (full).```\n"
                "Dengan catatan set harga gamepass akan melebihi pembelian untuk membayar tax "
                "yang ditanggung oleh kami, saat transaksi akan diintruksikan oleh kami."
            ),
            inline=False
        )

        await message.channel.send(embed=embed)

    # COMMUNITY ROBUX INSTANT
    elif content.startswith("!community"):
        robux_emoji = discord.utils.get(message.guild.emojis, name="robux")
        emoji_str = str(robux_emoji) if robux_emoji else "💰"

        embed = discord.Embed(
            title="# ROBUX INSTANT VIA COMMUNITY",
            description=(
                "**Robux Akan Langsung Masuk Tanpa Pending Tanpa Pajak (instant)**\n"
                "100% Clean, Guaranteed Anti CC/Phising\n\n"
                f"{emoji_str} Minimal pembelian 1000 robux\n"
                f"{emoji_str} 10.000+ ? open negotiable on ticket"
            ),
            color=discord.Color.purple()
        )
        await message.channel.send(embed=embed)

    # QRIS
    elif content.startswith("!qris"):
        embed = discord.Embed(
            title="📲 QRIS PAYMENT",
            description="Scan QR di bawah untuk melakukan pembayaran via QRIS.",
            color=discord.Color.orange()
        )
        embed.set_image(
            url="https://media.discordapp.net/attachments/1401733300225314946/1408387554595831859/IMG_9026.png?ex=68a98e9f&is=68a83d1f&hm=6ceabd95da99980dc9f53bf847be17411ae4e8f2a5825078f834b6669dce9181&=&format=webp&quality=lossless&width=669&height=943"
        )
        await message.channel.send(embed=embed)

client.run(TOKEN)


