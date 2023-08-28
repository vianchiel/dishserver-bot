import requests
import discord

class Discord_Interface:
    def __init__(self):
        # Credentials
        self.api_key = None
        self.token = None

        # Discord variables
        self.client = discord.Client()
        self.on_ready = self.client.event(self.on_ready)
        self.on_message = self.client.event(self.on_message)
    
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.client))

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        print(message.content)
        await message.channel.send('Hello! ' + message.author.name)

    def run(self):
        self.client.run("Token")
    