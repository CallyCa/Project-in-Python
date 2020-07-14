import discord, asyncio
from discord.ext import commands
import random

time = []

class comando(commands.Cog):
    
    # cria o construtor na classe
    def __init__(self, client):
        self.client = client
 

    @commands.guild_only()
    @commands.command()
    async def reg(self, ctx):
        user = self.client.db.users.find_one({"_id":ctx.author.id})
        if(user is None):
            self.client.db.users.insert_one({"_id":ctx.author.id, "coins":0})
            await ctx.send(f"Olá {ctx.author.mention}, você foi registrado")
        else:
            await ctx.send(f"Olá {ctx.author.mention}, você já foi registrado")
  

    @commands.guild_only()
    @commands.command()
    async def saldo(self, ctx):
        user = self.client.db.users.find_one({"_id":ctx.author.id})
        if(user is None):
            self.client.db.users.insert_one({"_id":ctx.author.id, "coins":0})
            await ctx.send(f"Olá {ctx.author.mention}, você não está registrado, digite !reg para se registrar")
        else:
            await ctx.send(f"Olá {ctx.author.mention}, você tem {user['coins']} coins")
    

    @commands.guild_only()
    @commands.command()
    async def mine(self, ctx):
        user = self.client.db.users.find_one({"_id":ctx.author.id})
        if(user is None):
            self.client.db.users.insert_one({"_id":ctx.author.id, "coins":0})
            await ctx.send(f"Olá {ctx.author.mention}, você não está registrado, digite !reg para se registrar")
        else:
            if(not ctx.author.id in time):
                coins = random.randint(1,10)
                self.client.db.users.update_one({"_id":ctx.author.id}, {"$inc":{"coins":coins}})
                await ctx.send(f"Olá {ctx.author.mention}, você ganhou {coins} coins")
                time.append(ctx.author.id)
                await asyncio.sleep(10)
                time.remove(ctx.author.id)
                await ctx.send(f"Olá {ctx.author.mention}, você precisa aguardar 10 segundos.")
  

def setup(client):
    client.add_cog(comando(client))
