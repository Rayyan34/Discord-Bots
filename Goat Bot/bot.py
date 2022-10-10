import discord
from goat import search


TOKEN = 'OTg5MTEwODk1MDU1NjI2Mjgw.G0RcQ2.nwD3VTLMXi3p_c0xLRddhu_AN_g8FJLPAOTf4M'
CHANNEL_ID = 982261403123605564

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id != CHANNEL_ID:
        return
    
    if message.content.split(' ')[0] == '!goat':
        item = message.content.replace('!goat ', '')

        product = search(item)

        embed = discord.Embed(
            title=product['value'],
            url='https://www.goat.com/sneakers/' + product['data']['slug']
        )
        embed.set_thumbnail(
            url = product['data']['image_url']
        )
        embed.add_field(
            name='Retail Price ($)',
            value = product['data']['retail_price_cents']/100
        )

        await message.channel.send(embed=embed)

client.run(TOKEN)