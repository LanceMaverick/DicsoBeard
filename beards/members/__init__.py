import csv
from time import sleep
import numpy as np
import pandas as pd
from discobeard.beards import Plugin

class Members(Plugin):
    
    def register_commands(self):
       self.commands = [
               ('members', self.get_member_list),
               ('membermatrix', self.get_member_matrix),
               ('membertable', self.get_member_table)
               ]

    async def get_member_list(self, client, message, args):
        members = message.server.members
        if args:
            role = ' '.join(args)
            names = u', '.join([m.name for m in members if role in [r.name for r in m.roles]])
        else:
            names = u', '.join([m.name for m in members])
        
        replies = self.msg_split(names, delim=', ')

    async def get_member_matrix(self, client, message, args):
        roles = message.server.roles
        members = message.server.members
        
        data = [['']+[r.name for r in roles]]
        for i, m in enumerate(members):
            data.append([m.name.encode()])
            for r in roles:
                if r in m.roles:

                    data[i+1].append(r.name.replace('=', '', 2))
                else:
                    data[i+1].append('')

        with open("x51.csv", "w") as outfile:
            writer = csv.writer(outfile)
            header = [x.replace('=', '', 2) for x in data.pop(0)]
            writer.writerow(header)
            writer.writerows(data)
        with open("x51.csv", "rb") as sendfile:
            await client.send_file(message.channel, sendfile, content="X51 roster:")

    async def get_member_table(self, client, message, args):
        roles = message.server.roles
        members = message.server.members
        
        data = []
        for i, m in enumerate(members):
            data.append([m.name.encode()])
            for r in roles:
                if r in m.roles:
                    data[i].append(r.name.replace("=", "", 2))
        
        with open("x51.csv", "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(data)
        with open("x51.csv", "rb") as sendfile:
            await client.send_file(message.channel, sendfile, content="X51 roster:")

    #factor out into helpers (make a generator?)
    def msg_split(self, msg, delim = ' ', max_length=200):
        words = iter(msg.split(delim))
        lines, current = [], next(words)
        for word in words:
            if len(current) + 1 + len(word) > max_length:
                lines.append(current)
                current = word
            else:
                current += delim + word

        lines.append(current)
        return lines


        
        
        




