import discord
from discord.ext import commands
import traceback
import sys

intents = discord.Intents.default()
#Message content intent needs to be enabled in the developer portal for your chosen bot.
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

bot.remove_command("help")

DISCORD_TOKEN = 'MTA5NDMxNTkyMTgxODAxMzc0Ng.GG4ZAd'

initial_extensions = ['cogs.voice']

@bot.event
async def on_ready():
    print('Вы вошли как')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f'Загружено {extension}')
        except Exception as e:
            print(f'Не удалось загрузить расширение {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run(DISCORD_TOKEN)
