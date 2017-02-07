import skbapi

async def broadcast_game(client, message, args = None):
    user_msg = None
    game_msg = None
    msg_list = []
    if args:
        user_msg = ' '.join(args)
    user = message.author.name
    game = message.author.game
    
    #for testing
#    game = Game()
    
    skb = skbapi.Skb()
    
    if user_msg:
        msg_list.append('*Sender:*\n{}'.format(user))
        msg_list.append('*Message:*\n{}'.format(user_msg))
    
    if game:
        msg_list.append('{} is currently playing *{}*.'.format(
                user,
                game.name))
    else:
        msg_list.append('{} is not currently in a game'.format(
                user))

    if not msg_list:
        await client.send_message(
                message.channel, 
                'I have no information to send.')
        return

    skb.send_message('\n'.join(msg_list))

async def hello(client, message, args):
    await client.send_message(message.channel, 'Hello!')


class Game:
    """test class"""
    name = 'Dota 2'
