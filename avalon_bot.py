# Work with Python 3.6
import os
import discord
import asyncio
import time
# import requests
# from datetime import datetime, timedelta
# from dateutil.parser import parse
from dotenv import load_dotenv
import util
import pyfiglet
import re
import secrets
load_dotenv(verbose=True)
token = os.getenv('token')

join_pattern = re.compile(r'^\$join [\w]{8}$')
client = discord.Client()
games = {}
gamesQ = []

class Game:
    roles = {}

    def __init__(self, code, channel):
        self.players = set()
        self.code = code
        self.channel = channel
    
    def __eq__(self, other):
        if isinstance(other, Game):
            return self.get_code() == other.get_code()
        return False
    
    def add_player(self, member):
        self.players.add(member)
    
    def has_player(self, member):
        return member in self.players
    
    def get_code(self):
        return self.code


@client.event
async def on_message(message):
    author = message.author
    if author == client.user:
        return
    channel = message.channel
    text = message.content.strip()
    if text.startswith('~hello'):
        msg = "Hello {0}".format(author.mention) + ", welcome to IRC Avalon!"
        await client.send_message(channel, msg)
    elif text.startswith('~new'):
        await new_game(channel, author)
    elif text.startswith('~join'):
        await join_game(channel, author, text)
    elif text.startswith("~debug"):
        await client.send_message(channel, len(gamesQ))

async def new_game(channel, author):
    msg = "```" + pyfiglet.figlet_format('Ava\nlon', font='smisome1') + "```"
    code = secrets.token_hex(4)
    new_game = Game(code, channel)
    new_game.add_player(author)
    games[code] = new_game
    gamesQ.insert(0, code)
    msg += "\n\n{0} started a new Avalon game! Use `~join {1}` to join the game. Use `~start {1}` to start the game with the players that have joined.".format(author.mention, code)
    await client.send_message(channel, msg)

async def join_game(channel, author, text):
    if not join_pattern.match(text):
        await client.send_message(channel, "Command formatting error. Please make sure to copy the join command exactly.")
    code = text[-8:]
    game = games[code]
    if game.has_player(author):
        await client.send_message(channel, "{0} is already in the game!".format(author.mention))
    else:
        game.add_player(author)
        await client.send_message(channel, "{0} joined the game!".format(author.mention))

async def prune_old_games():
    await client.wait_until_ready()
    while not client.is_closed:
        while len(gamesQ) > 5:
            gamesQ.pop()
        await asyncio.sleep(20)

@client.event
async def on_ready():
    print('-'*20)
    print('Logged in as', client.user.name)
    print(client.user.id)
    print('-'*20)

# Create a background task (i.e. doesn't require use input)
client.loop.create_task(prune_old_games())
client.run(token)