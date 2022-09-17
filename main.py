import os
from dotenv import load_dotenv
from discord.ext import commands
import discord.utils

import random


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(
    help='Helps determine if bot is actually alive or not',
    brief='Prints pong back to the channel'
)
async def ping(ctx): # ctx is context: message, channel, server, author, etc
    await ctx.channel.send('pong from vscode')


@bot.command(
help='The bot randomly chooses number between 0 and 10 and user has to guess it. User has 3 attempts',
brief='Game of guessing number'
)
async def numbers(ctx):
    attempts = 2
    num = random.randint(0, 10)
    await ctx.channel.send('Guess number from 0 to 10')
    print(num)
    while attempts >= 0:
        val = await bot.wait_for('message')
        guess = int(val.content)
        if 0 < guess > 10:
            await ctx.channel.send('You entered invalid number!')
        else:
            if guess == num:
                await ctx.channel.send('You win!')
                attempts = -1
            else:
                if attempts > 0:
                    attempts -= 1
                    await ctx.channel.send(f'Try again! You have {attempts+1} more attempts')
                else:
                    await ctx.channel.send(f'Unfortunately, you guessed wrong. The number was {num}')
                    attempts = -1

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    channel = bot.get_channel(896077052250296360)
    members = channel.members
    memb_ids = []
    for member in memb_ids:
        memb_ids.append(member.id)
    print(memb_ids)



@bot.command(
brief='Leaves voice channel'
)
async def stop(ctx):
    guild = ctx.guild.voice_client
    await guild.disconnect()

load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))