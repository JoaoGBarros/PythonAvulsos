import asyncio
import discord
from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import get


Intents = discord.Intents().all()
Intents.members = True
Intents.presences = True
client = discord.Client(intents=Intents)
keywords = ["joao", "esguicho", "karla", "bbb", "oi", "felippe"]

mensagens = {"Jowgabs#9263": "Joaozinho, o rei, chegou! <:BUU:749808231957659669> <:BUU:749808231957659669>  ",
             "Otoch#3732": "Olha o huguinho, a lenda :cowboy::cowboy:",
              "Karla#7116": "Karla, a rainha de tudo e todos esta aqui! :crown: :crown: ",
             "fleonemaia#0442": "Vovo ta cansado, ne fio :older_man: :older_man: "}




def is_spam(m):
    if m.content == "Caiu na maracutaia do bot de spam OTARIO":
        return True
    elif m.content == "Joao eh o maioral! :sunglasses: :sunglasses:":
        return True
    else:
        return False


async def apagaMsg(channel):

    await channel.purge(limit=25, check=is_spam)



@client.event
async def on_message(message):
    for word in keywords:
        if word in message.content:
            await message.channel.send("Caiu na maracutaia do bot de spam OTARIO")
            for i in range(5):
                await message.channel.send("Joao eh o maioral! :sunglasses: :sunglasses:")

    await asyncio.sleep(3)
    await apagaMsg(message.channel)


@client.event
async def on_member_update(before, after):
    if before.raw_status != "online":
        if after.raw_status == "online":
            pessoa = after.name + "#" + after.discriminator
            for usuario in mensagens.keys():
                if usuario == pessoa:
                    string = "**" + mensagens[pessoa] + "**"
                    await envia(string)

async def envia(string):
    channel = client.get_channel(704027732756922428)
    await channel.send(string)


async def bemvindo(member):
  channel = client.get_channel(704027732756922428)
  st = "**Ola, " + member.display_name + "! Bem Vindo ao server do Proc!! Sua role designida eh " + member.top_role.name +"**"
  await channel.send(st)

@client.event
async def on_member_join(member):
  role = get(member.guild.roles, name="Bamboli")
  await member.add_roles(role)
  await bemvindo(member)


keep_alive()
client.run('')
