"""
Discord bot
Riot API Link: https://developer.riotgames.com/
Discord Dev portal: https://discordapp.com/developers/applications/646587198422122496/bots
Useful discord reference: https://discordpy.readthedocs.io/en/latest/migrating.html#migrating-1-0-sending-messages
"""
import discord
import requests
import os

from dotenv import load_dotenv
load_dotenv()
#Getting API Tokens from a .env file for security reasons
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RIOT_TOKEN = os.getenv('RIOT_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!sup'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    #Check's the user's level
    if message.content.startswith('!level'):
        summoner_name = message.content.split("!level ", 1)[1]
        summoner_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + RIOT_TOKEN)
        print(response)
        responseJSON2 = response.json()
        print(responseJSON2)
        level = responseJSON2['summonerLevel']
        await message.channel.send("```" + summoner_name + "'s Level is: " + str(level) + "```")

    #WIP
    if message.content.startswith('!summoner'):
        summoner_name = message.content.split("!level ", 1)[1]
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + RIOT_TOKEN)
        responseJSON2 = response.json()
        response2 = requests.get("https://na1.api.riotgames.com" + "?api_key=" + RIOT_TOKEN)

        level = responseJSON2['summonerLevel']
        await message.channel.send("```" + summoner_name + "'s Level is: " + str(level) + "```")


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

client.run(DISCORD_TOKEN)
