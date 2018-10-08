from discobeard.beards import Plugin
from time import sleep

class Members(Plugin):
    
    def register_commands(self):
       self.commands = [
               ('members', self.get_member_list)]

    async def get_member_list(self, client, message, args):
        members = message.server.members
        if args:
            role = ' '.join(args)
            names = u', '.join([m.name for m in members if role in [r.name for r in m.roles]])
        else:
            names = u', '.join([m.name for m in members])
        
        replies = self.msg_split(names, delim=', ')
        #for r in replies:
        #    await client.send_message(message.channel, r.encode('utf-8'))

#        self.relay_message('\n'.join(msg_list))

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
        
        
        




