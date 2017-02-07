#!/usr/bin/env python
import asyncio
import discord
import cmd_funcs
import config

client = discord.Client()

#command functions [(funciton, command)]
beard_list = [
        (cmd_funcs.broadcast_game, 'broadcast'),
        (cmd_funcs.hello, 'hello'),
        ]

@client.event
async def on_ready():
    print('{} bot connected...'.format(client.user.name))

@client.event
async def on_message(message):
    if message.content.startswith('/'):
        args = message.content.split(' ')
        cmd = args.pop(0).strip('/') 
        for beard, command in beard_list:
            if command == cmd:
                await beard(client, message, args)


client.run(config.token)
