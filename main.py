import os
my_secret = os.environ['DISCORD_BOT_SECRET']
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 920461732420411422  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
    if message.author == bot.user:
      return

    if message.content.startswith('!hello'):
      await message.channel.send('Hello!')

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.
my_secret = os.environ['DISCORD_BOT_SECRET']
keep_alive()  # Starts a webserver to be pinged.

