from discobeard.beards import Plugin

class BroadCast(Plugin):
    
    def register_commands(self):
       self.commands = [
               ('broadcast', self.broadcast_game)]

    async def broadcast_game(self, client, message, args):
        user_msg = None
        game_msg = None
        msg_list = []
        if args:
            user_msg = ' '.join(args)
        user = message.author.name
        try:
            game = message.author.game
        except AttributeError:
            game = None
            print('No game found')
        #game = Game()
        
        if user_msg:
            msg_list.append('*Sender:*\n{}\n'.format(user))
            msg_list.append('*Message:*\n{}\n'.format(user_msg))
        
        if game:
            msg_list.append('{} is currently playing *{}*.'.format(
                    user,
                    game.name))
#        else:
#            msg_list.append('{} is not currently in a game'.format(
#                    user))

        if not msg_list:
            await client.send_message(
                    message.channel, 
                    'I have no information to send.')
            return

        self.relay_message('\n'.join(msg_list))


#test class
class Game:
    name = 'World of Warships'
