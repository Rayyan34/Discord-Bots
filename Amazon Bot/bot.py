import discord
from amazon import search

token = 'OTg5NTMwNTEyNDA0MTI3ODI1.Gya76Q.zrMEriE4u2Hdn9UZr340aB2sEL5VZuR40X5Cew'
channel_id = 982261403123605564

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id != channel_id:
        return
    
    if message.content.split(' ')[0] == '!amazon':
        item = search(message.content.replace('!amazon', ''))

        embed = discord.Embed(
            title = item['title'],
            url = 'https://www.amazon.ae/' + item['url']
        )
        embed.set_thumbnail(
            url = item['image']
        )
        embed.add_field(
            name = 'Price',
            value = item['price']
        )

        await message.channel.send(embed=embed)

client.run(token)
