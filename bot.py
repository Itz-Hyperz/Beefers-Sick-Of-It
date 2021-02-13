import discord
import asyncio
from discord.ext import commands
from discord.utils import get
TOKEN = 'INSERT_TOKEN_HERE'
BOT_PREFIX = '.'

client = commands.AutoShardedBot(command_prefix=BOT_PREFIX)
client.remove_command("help")

async def presence_change():
    while True:
        guilds = len(client.guilds)
        activity = discord.Activity(type=discord.ActivityType.watching, name=f"{guilds} servers | .beef")
        await client.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(15)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")
    client.loop.create_task(presence_change())

@client.command(
    name='beef',
    description='Plays bliss in your ears',
    pass_context=True,
)
async def beef(context):
    channel = context.message.author.voice.channel
    await channel.connect()
    await context.channel.send("I joined the channel")
    guild = context.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('audio.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

client.run(TOKEN)
