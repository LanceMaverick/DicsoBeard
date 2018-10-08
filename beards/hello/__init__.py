from discobeard.beards import Plugin

class HelloWorld(Plugin):
    def register_commands(self):
       self.commands = [
               ('helloworld', self.hello_world)]

    async def hello_world(self, client, message, args):
        await client.send_message(message.channel, 'hello!')

