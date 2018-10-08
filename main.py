#!/usr/bin/env python
import os
import sys
from time import sleep
import importlib
import asyncio
import discord
import config
from discobeard.beards import Plugin

import logging
logger = logging.getLogger(__name__)

client = discord.Client()

def is_module(filename):
    fname, ext = os.path.splitext(filename)
    if ext == ".py":
        return True
    elif os.path.exists(os.path.join(filename, "__init__.py")):
        return True
    else:
        return False

def get_literal_path(path_or_autoloader):
    try:
        return path_or_autoloader.path
    except AttributeError:
        assert type(path_or_autoloader) is str, "beard_path is not a str or an AutoLoader!"
        return path_or_autoloader

def get_literal_beard_paths(beard_paths):
    return [get_literal_path(x) for x in beard_paths]

def all_possible_beards(paths):
    literal_paths = get_literal_beard_paths(paths)

    for path in literal_paths:
        for f in os.listdir(path):
            if is_module(os.path.join(path, f)):
                yield os.path.basename(f)

for beard_path in config.beard_paths:
    sys.path.insert(0, get_literal_path(beard_path))

logger.info("Loaded the following plugins:\n {}".format(
    ', '.join(list(all_possible_beards(config.beard_paths)))))
logger.info("config.beards: {}".format(config.beards))

if config.beards == "all":
    for beard_name in all_possible_beards(config.beard_paths):
        importlib.import_module(beard_name)
else:
    for beard_name in config.beards:
        importlib.import_module(beard_name)

for beard_path in config.beard_paths:
    sys.path.pop(0)

#command functions [(funciton, command)]

cmds = []
@client.event
async def on_ready():
    print('Mounting dicobeard plugins.')
    for beard in Plugin.plugins:
        if beard.commands:
            cmds.extend(beard.commands)
    print('{} bot connected...'.format(client.user.name))


@client.event
async def on_message(message):
    if message.content.startswith('/'):
        args = message.content.split(' ')
        cmd = args.pop(0).strip('/') 
        for command, coro in cmds:
            if command == cmd:
                await coro(client, message, args)

if __name__ == "__main__":
    client.run(config.token)
