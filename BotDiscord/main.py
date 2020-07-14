import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or
import pymongo

modulos = ["cogs.comando"]

# Evento do client
client = AutoShardedBot(command_prefix="!", case_insensitive = True)

# evento do on_ready
@client.event

async def on_ready():
    print(f"{client.user.name} Online hihi.")
    await client.change_presence(activity = discord.Streaming(name = "!help", url="https://www.twitch.tv/123"))



client.db = pymongo.MongoClient("Informe sua Database")["discord"]



if  __name__ == "__main__":
    for modulo in modulos:
        # Função para carregar um modulo
        try:
            client.load_extension(modulo)
        except Exception as e:
            print("Erro ao carregar cog {modulo}\nErro:{e}")



# Irá coletar o token do bot
    client.run("Informe seu token")
