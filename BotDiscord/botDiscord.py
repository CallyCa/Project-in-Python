# Importao modulo discord
import discord
import asyncio
import random

# Aqui irá criar uma conexão com o cliente do discord
client = discord.Client()

# Aqui irá registrar um evento
@client.event

# on_ready irá deixar o bot em estado de pronto - online
async def on_ready(): 
    print("Bot online")
    # Aqui irá imprimir o nome do bot
    print(client.user.name)
    # Imprime o  ID do bot
    print(client.user.id)
    print("\n")

# Registra um evento
@client.event

# O evento on_message é chamado quando o bot recebe uma mensagem
async def on_message(message):
    #
    if(message.content.lower().startswith('?test')):
        await message.channel.send("Olá - Bot criado por cally hihi")
        await message.channel.send("Só nos python")
        await message.channel.send("O que você deseja?")

    
# message.content irá atribuir ?moeda 
# .lower converte todos os caracteres maiúscullos para minusculo e retorna
# .startswith retorna True quando o Prefixo como "?moe" for verdadeiro
# retorna False quando o prefixo
    if(message.content.lower().startswith('?moeda')):
        if(message.author.id == "Seu id"):
            choice = random.randint(1,2)
            if(choice == 1):
                await message.add_reaction('😀')
            if(choice == 2):
                await message.add_reaction('👑')
        else:
            await message.channel.send("Você não tem permissão para este comando.")




client.run("ID BOT")
