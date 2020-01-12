"""
Discord bot
Riot API Link: https://developer.riotgames.com/
Discord Dev portal: https://discordapp.com/developers/applications/646587198422122496/bots
Useful discord reference: https://discordpy.readthedocs.io/en/latest/migrating.html#migrating-1-0-sending-messages
Test
"""
import discord
import requests

TOKEN = 'NjQ2NTg3MTk4NDIyMTIyNDk2.XdTmOQ.4xPWz9K6TvUtZZlo8-w-s41OOWQ'
riot_token = 'RGAPI-f95d7f3a-6285-4cd6-b1bf-ee6a87288b83'
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!sup'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!level'):
        summoner_name = message.content.split("!level ", 1)[1]
        response = requests.get("https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/" + summoner_name + "?api_key=" + riot_token)
        responseJSON2 = response.json()
        level = responseJSON2['summonerLevel']
        await message.channel.send(summoner_name + "'s Level is: " + str(level))

    if message.content.startswith('!Derpdot'):
        msg = 'Derpdot is the coolest guy i know'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!help'):
        msg = '!level: Retrieve\'s a Summoner\'s level'
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
