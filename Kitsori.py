import discord
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='!!')  


TOKEN = "NTkxNjk5MTQxOTQ0NTQxMzkz.XQ0mLA.GA8s9_jEljMxT9qzndzbwo7NXPM"  # Nn passar para ninguem

 
@bot.event
async def on_ready():
    print('O Bot:')
    print(bot.user.name)
    print(bot.user.id)
    print('Está online no momento')
 


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Salve {member.name}, seja bem vindo!'
    )

@bot.command(name='uniao flasco', help='Cante junto com o bot')
async def uniao_flasco(Ctx):
    uniao_flasco_letra: [
         'mano sem caô, batendo punheta com o pau no ventilador'
         ]
    response = random.choice(unia_flasco_letra)
    await ctx.send(response)    

@bot.command(name='dado', help='jogue um dado, escolhendo a quantidade de dados e quantos lados eles tem')
asyc def dado(ctx, numero_de_dados, numero_de_lados):
 dado = [
     str(random.choice(range(1, numero_de_dados + 1)))
     for _ in range(numero_de_dados)
 ]
 await ctx.send (' , '.join(dado))

@bot.command(name='Criar-sala')
@commands.has_role('adm')
async def create_channel(ctx, channel_name='Nova-sala'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Criando uma nova sala: {channel_name}')
        await guild.create_text_channel(channel_name)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Você não tem cargo de adm.')        


bot.run('TOKEN')
