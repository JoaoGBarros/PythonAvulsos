import asyncio
from discord.ext import commands
#from keep_alive import keep_alive
from discord.utils import get
import datetime
import discord


Intents = discord.Intents().all()
Intents.members = True
Intents.presences = True
client = discord.Client(intents=Intents)
keywords = ["!joao", "!otoch", "!comandos"]
msg_apagar = ["Caiu na maracutaia do bot de spam OTARIO", "Joao eh o maioral! :sunglasses: :sunglasses:",
              "Vai se fuder Otoch"]


mensagens = {"Jowgabs#9263": "Joaozinho, o rei, chegou! <:BUU:749808231957659669> <:BUU:749808231957659669>  ",
             "Otoch#3732": "Olha o huguinho, a lenda :cowboy::cowboy:",
              "Karla#7116": "Karla, a rainha de tudo e todos esta aqui! :crown: :crown: ",
             "fleonemaia#0442": "Vovo ta cansado, ne fio :older_man: :older_man:",
             "Gianluca#1828": "Peruanos saiam do servidor, ELE chegou",
             "Aang#5019": "Olha o avatar fumando um baseado eh o ",
             "Pietroluongo#3808": "O maior de todos: ",
             "VictorAg#5290": "Olha se nao eh a mocoronga e a baranguinha <:lorena:771380590716125200> ",
             "Esguicho4#8105": "Vai fazer gol com o corsinha "}


token =''


def is_spam(m):
    for mens in msg_apagar:
        if m.content == mens:
            return True

    return False

async def apagaMsg(channel):
    await channel.purge(limit=25, check=is_spam)



@client.event
async def on_message(message):
    for word in keywords:
        if word in message.content and message.content != "!otoch":
            await message.channel.send("Caiu na maracutaia do bot de spam OTARIO")
            for i in range(5):
                await message.channel.send("Joao eh o maioral! :sunglasses: :sunglasses:")
        elif word in message.content and message.content == "!otoch":
            for i in range(5):
              await message.channel.send("Vai se fuder Otoch")
        elif word in message.content and message.content == "!comandos":
            for comandos in keywords:
                if comandos != "!comandos":
                    message.channel.send(comandos + " - Testa ai parceiro")
                else:
                    message.channel.send(comandos + " - Mostra os comandos, mais por vir!")

    await asyncio.sleep(3)
    await apagaMsg(message.channel)


@client.event
async def on_member_update(before, after):
    if before.raw_status != "online":
        hr = datetime.time.now().time().strftime("%H")
        if after.raw_status == "online" and hr >= 2:
            pessoa = after.name + "#" + after.discriminator
            for usuario in mensagens.keys():
                if usuario == pessoa:
                    string = "**" + mensagens[pessoa] + "**" + after.mention
                    await envia(string)


async def envia(string):
    channel = client.get_channel(704027732756922428)
    await channel.send(string)


async def bemvindo(member):
  channel = client.get_channel(704027732756922428)
  st = "**Ola, " + member.display_name + "! Bem Vindo ao server do Proc!! Sua role eh " + member.top_role.name +"**"
  await channel.send(st)

@client.event
async def on_member_join(member):
  role = get(member.guild.roles, name="Bamboli")
  await member.add_roles(role)
  await bemvindo(member)


#keep_alive()
client.run('')
