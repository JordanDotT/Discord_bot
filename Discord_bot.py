"""
Discord bot
Riot API Link: https://developer.riotgames.com/
Discord Dev portal: https://discordapp.com/developers/applications/646587198422122496/bots
Useful discord reference: https://discordpy.readthedocs.io/en/latest/migrating.html#migrating-1-0-sending-messages
"""
import discord

TOKEN = 'TOKEN'
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!sup'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
