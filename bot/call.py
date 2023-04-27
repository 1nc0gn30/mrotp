import os
import discord
from discord.ext import commands
from twilio.rest import Client
from pyngrok import ngrok

# Enter your Twilio account SID and auth token
account_sid = "TWILIO SID"
auth_token = "TWILIO TOKEN"
client = Client(account_sid, auth_token)

# Enter the phone number to make the call to
to_phone_number = "PHONE NUMBER TO CALL"

# Create a Discord bot client
intents = discord.Intents.all()
intents.members = True
intents.guild_messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Set up ngrok tunnel
ngrok_tunnel = ngrok.connect(8080, bind_tls=True, bind_addr='0.0.0.0')


# Define a command to make the call
@bot.command()
async def call(ctx):
    # Make the call using Twilio
    call = client.calls.create(
        to=to_phone_number,
        from_="TWILIO NUMBER",
        url="NGROK TUNNEL TO XML FILE"
    )

    # Send a message to the Discord server confirming the call has been made
    await ctx.send(f"Calling {to_phone_number}...")

# Run the Discord bot
bot.run("DISCORD BOT TOKEN")
