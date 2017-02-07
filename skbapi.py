import requests
import json
import apiconfig as config

class Skb:
    """A very simple WIP wrapper for making requests to
    skybeard"""
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url', config.url)
        self.key = kwargs.get('key', config.skb_key)
        self.chat_id = kwargs.get('chat_id', config.default_chat)
        self.endpoints = {
                'send_message': '/sendMessage',}

    def send_message(
            self, 
            text, 
            parse_mode='markdown', 
            header = '*Message from discord:*\n'):

        request_url = self.url+self.endpoints['send_message']
        payload = {
                'key': self.key,
                'text': header+text,
                'chat_id': self.chat_id,
                'parse_mode': parse_mode
                }

        response = requests.post(request_url, json.dumps(payload))
        return response



    

