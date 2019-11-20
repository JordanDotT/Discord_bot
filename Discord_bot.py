# Work with Python 3.6
import discord

TOKEN = 'NjQ2NTg3MTk4NDIyMTIyNDk2.XdTZAQ.PEBMMNUBWyN8ww04iB55kEmT-iI'

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