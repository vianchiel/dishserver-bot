# Core Libraries
import os
import requests
import random

# Discord Libraries
import discord

class Discord_Interface:
    def __init__(self, config):
        # Credentials
        self.token      = config['TOKEN']
        self.guildname  = config['GUILD']
        self.perms_int  = config['PERMISSIONS_INTEGER']

        # Discord variables
        self.client = discord.Client(
            intents = discord.Intents().all(),
            )
        self.on_ready = self.client.event(self.on_ready)
        self.on_message = self.client.event(self.on_message)

        # Discord Servers
        self.guild = None
    
    async def on_ready(self):
        # Display welcome message
        print('Logged in as {0.user}'.format(self.client))

        # Retrieve list of servers
        self.guild = [guild for guild in self.client.guilds]

        # Display list of servers
        print('Available Guilds:')
        for guild in self.guild:
            print('\t' + guild.name)

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.content.lower().startswith("cheese curds"):
            print(message)
            luckyman = random.choice(
                [member for member in message.guild.members]
                )
            
            embed = discord.Embed(
                colour=discord.Colour.dark_teal(),
                title="Congratulations " + luckyman.display_name + "!",
                description="You are chosen to purchase Quails Cheese Curds!"
            )

            await message.channel.send("<@!" + str(luckyman.id) + ">",embed=embed)

    def run(self):
        self.client.run(self.token)
    

