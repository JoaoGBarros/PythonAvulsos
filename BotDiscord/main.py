import asyncio
import discord

Intents = discord.Intents().all()
Intents.members = True
Intents.presences = True
client = discord.Client(intents=Intents)
keywords = ["joao", "esguicho", "karla", "bbb", "oi", "felippe"]

mensagens = {"Jowgabs#9263": "Joaozinho, o rei, chegou! Vassalos comecem as reverencias! :star_struck: :star_struck:  ",
             "Otoch#3732": "Olha o huguinho, a lenda :cowboy::cowboy:",
              "Karla#7116": "Karla, a rainha de tudo e todos esta aqui! :crown: :crown: ",
             "fleonemaia#0442": "Vovo ta cansado, ne fio :older_man: :older_man: "}


token = 
async def apagaMsg(message):
    for i in range(6):
        if str(message.channel) == "geral" and (message.content == "Caiu na maracutaia do bot de spam OTARIO"
                                                or message.content == "Joao eh o maioral! :sunglasses: :sunglasses:"):

            await message.channel.purge(limit=1)


@client.event
async def on_message(message):
    for word in keywords:
        if word in message.content:
            await message.channel.send("Caiu na maracutaia do bot de spam OTARIO")
            for i in range(5):
                await message.channel.send("Joao eh o maioral! :sunglasses: :sunglasses: ")

    await asyncio.sleep(4)
    await apagaMsg(message)


@client.event
async def on_member_update(before, after):
    if before.raw_status != "online":
        if after.raw_status == "online":
            pessoa = after.name + "#" + after.discriminator
            for usuario in mensagens.keys():
                if usuario == pessoa:
                    await envia(pessoa)

async def envia(pessoa):
    channel = client.get_channel(704027732756922428)
    await channel.send(mensagens[pessoa])

client.run(token)
