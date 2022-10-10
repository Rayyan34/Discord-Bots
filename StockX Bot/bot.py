import discord
from stockx import search

token = "OTgyMjYwMDM4MDE2MDUzMjQ4.GowWzj.N-GqhAExqVpzzt8NBhj5OIDtYGEnTV4lyGbNRo"

client = discord.Client()

channel_id = 982261403123605564

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id != channel_id:
        return

    if message.content.split(' ')[0] == '!stockx':
        query = message.content.replace('!stockx ', '')

        item = search(query)

        embed = discord.Embed(
            title = item['title'],
            url='https://stockx.com/' + item['urlKey']
        )
        embed.set_thumbnail(
            url = item['media']['imageUrl']
        )
        embed.add_field(
            name = 'Colorway',
            value=item['colorway']
        )
        embed.add_field(
            name = 'Style ID', 
            value = item['styleId']
        )
        embed.add_field(
            name = 'Last Sale',
            value = item['market']['lastSale']
        )
        await message.channel.send(embed=embed)

client.run(token)