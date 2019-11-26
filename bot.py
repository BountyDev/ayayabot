import discord
import random
import os
import json
import urllib.request
import urllib.parse
import re
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import time

client = commands.Bot(command_prefix = '-')
amounts = {}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("hecc da police"))
    print("ONLINE")

@client.event
async def on_member_join(member):
    print('Welcome')

@client.event
async def on_member_remove(member):
    print(f'Begone {member} u hecc')

@client.command()
async def youtube(ctx, *, link = None):
    query_string = urllib.parse.urlencode({"search_query" : link})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    await ctx.send(f"http://www.youtube.com/watch?v={search_results[0]}")

@client.command()
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You are missing an argument')

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def ayayaping(ctx):
    await ctx.send(f'Ayaya Ayaya yo ping is {round(client.latency * 1000)}')

@client.command()
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
async def ayayasad(ctx):
    await ctx.send('https://tenor.com/PSny.gif')

@client.command()
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
async def owners(ctx):
    embed = discord.Embed(title="**Owners**", description="♡ ===【Go follow all the Owners】=== ♡", color=663399)
    with open('owners.json') as f:
        owners = json.load(f)
    num = 1
    while num < len(owners)+1:
        nick = "**"+owners[str(num)].split("~")[2]+"**"
        link = owners[str(num)].split("~")[1]
        owner = owners[str(num)].split("~")[0]
        embed.add_field(name=nick, value=link, inline=False)
        num+=1
    await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_roles=True, manage_messages=True)
async def addowner(ctx, nick = None, link = None, owner = None):
    if owner != None or link != None or nick != None:
        with open('owners.json') as f:
            owners = json.load(f)
        owners[len(owners)+1] = owner + "~" + link + "~" + nick
        await ctx.send(f"{owner} has been added as an owner")
        with open('owners.json', 'w+') as f:
            own = json.dump(owners, f)
    else:
        await ctx.send("Please fill out all commands addhosts(nick,link,owner)")

@client.command()
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
async def hosts(ctx):
    embed = discord.Embed(title="**Hosts**", description="♡ ===【Go follow all the Hosts】=== ♡", color=663399)
    with open('hosts.json') as f:
        owners = json.load(f)
    num = 1
    while num < len(owners)+1:
        nick = "**"+owners[str(num)].split("~")[2]+"**"
        link = owners[str(num)].split("~")[1]
        owner = owners[str(num)].split("~")[0]
        embed.add_field(name=nick, value=link, inline=False)
        num+=1
    await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_roles=True, manage_messages=True)
async def addhost(ctx, nick = None, link = None, owner = None):
    if owner != None or link != None or nick != None:
        with open('hosts.json') as f:
            owners = json.load(f)
        owners[len(owners)+1] = owner + "~" + link + "~" + nick
        await ctx.send(f"{owner} has been added as an host")
        with open('hosts.json', 'w+') as f:
            own = json.dump(owners, f)
    else:
        await ctx.send("Please fill out all commands addowner(nick,link,owner)")

@client.command()
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
async def mods(ctx):
    embed = discord.Embed(title="**Mods**", description="♡ ===【Go follow all the Mods】=== ♡", color=663399)
    with open('mods.json') as f:
        owners = json.load(f)
    num = 1
    while num < len(owners)+1:
        nick = "**"+owners[str(num)].split("~")[2]+"**"
        link = owners[str(num)].split("~")[1]
        owner = owners[str(num)].split("~")[0]
        embed.add_field(name=nick, value=link, inline=False)
        num+=1
    await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_roles=True, manage_messages=True)
async def addmod(ctx, nick = None, link = None, owner = None):
    if owner != None or link != None or nick != None:
        with open('mods.json') as f:
            owners = json.load(f)
        owners[len(owners)+1] = owner + "~" + link + "~" + nick
        await ctx.send(f"{owner} has been added as a mod")
        with open('mods.json', 'w+') as f:
            own = json.dump(owners, f)
    else:
        await ctx.send("Please fill out all commands addmod(nick,link,owner)")

@client.command()
@has_permissions(manage_roles=True, manage_messages=True)
async def removemod(ctx, owner = None):
    if owner != None:
        with open('mods.json') as f:
            owners = json.load(f)
        owners2 = {}
        num = 1
        num2 = 1
        while num<len(owners)+1:
            own = owners[str(num)].split("_")[1]
            ownname = owners[str(num)].split("_")[0]
            if own != owner:
                owners2[num2] = owners[str(num)]
                num2+=1
            else:
                await ctx.send(f"{ownname} has been removed")
            num+=1
        with open('mods.json', 'w+') as f:
            own = json.dump(owners2, f)
    else:
        await ctx.send("Please specify a mod's link")

@client.command()
async def test(ctx):
    embed = discord.Embed(title="**Hello Newcomers**", description="Embark on your journey towards becoming a true degenerate today!\n Please read ❗rules❗ before going anywhere! There's very special information there, especially for people who are new to discord!\n I recommend starting a conversation or maybe joining one in #♡「lounge」 , tell us a little about yourself and you will quickly find a home in this server!\n If you have any other questions, feel free to ask in chat or just DM an owner!", color=663399)
    message = await ctx.send(embed=embed)
    await asyncio.sleep(10)
    await message.delete()

@client.command()
async def instagram(ctx, user = None):
    if user != None:
        with open('owners.json') as f:
            owners = json.load(f)
        num = 1
        num2 = 1
        while num<len(owners)+1:
            own = owners[str(num)].split("~")[1]
            ownname = owners[str(num)].split("~")[0]
            if ownname == user:
                await ctx.send(f"{own}")
            num+=1
        with open('hosts.json') as f:
            owners = json.load(f)
        num = 1
        num2 = 1
        while num<len(owners)+1:
            own = owners[str(num)].split("~")[1]
            ownname = owners[str(num)].split("~")[0]
            if ownname == user:
                await ctx.send(f"{own}")
            num+=1
        with open('mods.json') as f:
            owners = json.load(f)
        num = 1
        num2 = 1
        while num<len(owners)+1:
            own = owners[str(num)].split("~")[1]
            ownname = owners[str(num)].split("~")[0]
            if ownname == user:
                await ctx.send(f"{own}")
            num+=1
    else:
        await ctx.send("Please specify an owner")

@client.command()
@has_permissions(manage_roles=True, manage_messages=True)
async def removeowner(ctx, owner = None):
    if owner != None:
        with open('owners.json') as f:
            owners = json.load(f)
        owners2 = {}
        num = 1
        num2 = 1
        while num<len(owners)+1:
            own = owners[str(num)].split("_")[1]
            ownname = owners[str(num)].split("_")[0]
            if own != owner:
                owners2[num2] = owners[str(num)]
                num2+=1
            else:
                await ctx.send(f"{ownname} has been removed")
            num+=1
        with open('owners.json', 'w+') as f:
            own = json.dump(owners2, f)
    else:
        await ctx.send("Please specify an owner's link")

@client.command()
@has_permissions(manage_roles=True, manage_messages=True)
async def removehost(ctx, owner = None):
    if owner != None:
        with open('hosts.json') as f:
            owners = json.load(f)
        owners2 = {}
        num = 1
        num2 = 1
        while num<len(owners)+1:
            own = owners[str(num)].split("_")[1]
            ownname = owners[str(num)].split("_")[0]
            if own != owner:
                owners2[num2] = owners[str(num)]
                num2+=1
            else:
                await ctx.send(f"{ownname} has been removed")
            num+=1
        with open('hosts.json', 'w+') as f:
            own = json.dump(owners2, f)
    else:
        await ctx.send("Please specify an owner's link")

@client.command()
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
async def loli(ctx):
        hug = ["https://tenor.com/Fj27.gif",
            "https://tenor.com/Pj92.gif",
            "https://tenor.com/PM1R.gif",
            "https://tenor.com/Oye8.gif",
            "https://tenor.com/u2et.gif",
            "https://tenor.com/IHEh.gif",
            "https://tenor.com/xw4M.gif",
            "https://tenor.com/Hbum.gif",
            "https://tenor.com/vzyG.gif"
            ]
        hug = random.choice(hug)
        await ctx.send(f"**FBI WE GOTTEM** {hug}")

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def ayayafortune(ctx):
    fortune =   ['**You have the big gay**',
                 '**Ayaya Ayaya Hecc u**',
                 '**U will get hit by a bus**',
                 '**You will commit dead**',
                 '**You will be partying in hell**',
                 '**You will eat your whole family**',
                 '**You will have a good day**',
                 '**Satan will possess you and kill your entire family**',
                 '**Komi-san is god**']
    url = 'https://tenor.com/IDsR.gif'
    await ctx.send(f'{url} \n {random.choice(fortune)}')

@client.command()
@has_permissions(manage_roles=True, manage_messages=True)
async def uwu(ctx, player: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Host")
    user = player
    await user.add_roles(role)

@client.command()
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def yandere(ctx):
        hug = ["https://tenor.com/9oII.gif",
            "https://tenor.com/17eH.gif",
            "https://tenor.com/17eB.gif",
            "https://tenor.com/17eK.gif"
            ]
        hug = random.choice(hug)
        await ctx.send(f"You into some weird shit :P {hug}")

@client.command(aliases=['clear'])
@has_permissions(manage_roles=True, manage_messages=True)
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def ayayaclear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Ayaya Ayaya {amount} messages have been removed')

@client.command(aliases=['slots'])
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
async def ayayaslots(ctx):
    slots = [':rage:',
             ':neutral_face: ',
             ':grinning:']
    slots1 = random.choice(slots)
    slots2 = random.choice(slots)
    slots3 = random.choice(slots)
    await ctx.send(f'{slots1},{slots2},{slots3}')
    if(slots1==slots2==slots3):
        await ctx.send('You win')
    else:
        await ctx.send('You lose')

@client.command()
async def jesus(ctx):
    jesus = random.randint(100000,999999)
    await ctx.send(f"Your daily number of jesus is {jesus}")

@client.command()
@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
async def hug(ctx, Player = None):
    if ctx.channel.id == 627306015011897364:
        if Player == None:
            await ctx.send("Please specify a weeb")
        else:
            hug = ["https://tenor.com/view/anime-hug-sweet-love-gif-14246498",
                "https://tenor.com/FQNP.gif",
                "https://tenor.com/Fipo.gif",
                "https://tenor.com/vksq.gif"
                ]
            hug = random.choice(hug)
            await ctx.send(f"**Heres a hug** {Player} {hug}")

@client.command()
@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
async def thigh(ctx):
    hug = ["https://66.media.tumblr.com/98b87caab8969a1f876677ae5bbc340b/tumblr_pvhaqjph2U1w2mu5po1_1280.jpg",
        "https://tenor.com/FQNP.gif",
        "https://tenor.com/Fipo.gif",
        "https://tenor.com/vksq.gif"
        ]
    hug = random.choice(hug)
    await ctx.send(f"**Heres a thigh** {hug}")

@client.command()
@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
async def incest(ctx, Player = None):
    if Player == None:
        await ctx.send("Please specify a weeb")
    else:
        hug = ["https://tenor.com/wDsb.gif"
            ]
        hug = random.choice(hug)
        await ctx.send(f"**If I were your sibling I would fuck you** {Player} {hug}")

@client.command()
@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
async def kiss(ctx, Player = None):
    if ctx.channel.id == 627306015011897364:
        if Player == None:
            await ctx.send("Please specify a weeb")
        else:
            hug = ["https://tenor.com/vxPx.gif",
                   "https://tenor.com/PIoc.gif",
                   "https://tenor.com/05fP.gif",
                   "https://tenor.com/39Ef.gif"
                ]
            hug = random.choice(hug)
            await ctx.send(f"**Heres a kiss** {Player} {hug}")

@client.command()
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def nezuko(ctx):
    hug = ["https://tenor.com/7O8f.gif",
           "https://tenor.com/7SYJ.gif",
           "https://tenor.com/80KV.gif",
           "https://tenor.com/9hTn.gif",
           "https://tenor.com/8aTM.gif",
           "https://tenor.com/view/kimetsu-no-yaiba-baby-nezuko-running-gif-14864027"
        ]
    hug = random.choice(hug)
    await ctx.send(f"**Nezuko!!** {hug}")

@client.command()
@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
async def yaoi(ctx):
    hug = ["https://gph.is/1hQvKA4",
           "http://gph.is/1LdEHB9",
           "https://gph.is/2cqcHDm",
           "https://gph.is/2ayws8A",
           "https://tenor.com/171Q.gif"
        ]
    hug = random.choice(hug)
    await ctx.send(f"**Uh yay YAOI!!** {hug}")

@client.command()
@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
async def headpat(ctx):
    hug = ["https://tenor.com/YAN5.gif",
           "https://tenor.com/MLKi.gif",
           "https://tenor.com/W2Am.gif",
           "https://tenor.com/view/anime-cute-pat-gif-5155410",
           "https://giphy.com/gifs/cute-headpat-104xeY1nIvrI64",
           "https://gifimage.net/wp-content/uploads/2017/09/anime-head-pat-gif.gif",
           "https://giphy.com/gifs/ARSp9T7wwxNcs"
        ]
    hug = random.choice(hug)
    await ctx.send(f"yey {hug}")

@client.command()
@commands.cooldown(rate=1, per=1, type=commands.BucketType.user)
async def yuri(ctx):
    hug = ["https://gph.is/28JtH1K",
           "https://gph.is/2cRuyUy",
           "https://gph.is/296yxdh",
           "https://gph.is/2cPzRkC",
           "https://gph.is/2cRsI5M",
           "http://66.media.tumblr.com/3301cae5d0d736240902d29651bd4c7d/tumblr_mqpxvgnIOY1rnhrswo1_500.gif",
           "https://tenor.com/view/anime-yuri-kissing-gif-14388725",
           "https://tenor.com/view/love-yuri-anime-gif-5101517",
           "https://tenor.com/6iv7.gif",
           "http://66.media.tumblr.com/c704c2278fceedf8730b5c0c73f8cd48/tumblr_njk7z5xcTF1u56h1mo2_500.gif",
           "http://66.media.tumblr.com/6f8ff86f36a0c7fa6f6cf2b6c4b00663/tumblr_n4go91rApi1sfqkpto1_500.gif",
           "https://tenor.com/view/sakura-trick-kiss-yuri-gif-11487318",
           "https://tenor.com/view/yuri-gif-5999933",
           "http://66.media.tumblr.com/26cd6427baea794c653f45b6941884cb/tumblr_n0slnzgRtM1tqfu4lo1_400.gif"
        ]
    hug = random.choice(hug)
    await ctx.send(f"**yes!!** {hug}")


#@client.command()
#@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
#async def ayayakick(ctx, member : discord.Member, *, reason=None):
#    await member.kick(reason=reason)
#    await ctx.send(f'{member} has been kicked')

#@client.command()
#@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
#async def ayayaban(ctx, member : discord.Member, *, reason=None):
#    await member.ban(reason=reason)
#    await ctx.send(f'{member} has been banned')

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def ayayacount(ctx):
    id = client.get_guild(356277136727867392)
    await ctx.send(f'There are {id.member_count} users, in this server')

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def ayayahelp(ctx):
    await ctx.send('**current commands:** areayayaslots, ayayafortune, ayayasad, ayayaping, ayayacount, ayaya, weeblevel')

#@client.command(pass_context=True)
#@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
#async def join(ctx):
#    channel = ctx.message.author.voice.voice_channel
#    await client.join_voice_channel(channel)

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def ayaya(ctx):
    await ctx.send('https://www.youtube.com/watch?v=9wnNW4HyDtg')

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def weeblevel(ctx):
    weeb = random.randint(0,100)
    await ctx.send(f'You are {weeb}% weeb')

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def gaylevel(ctx):
    gay = random.randint(0,100)
    if gay > 80:
        await ctx.send('Get yo gayness outta here')
    else:
        await ctx.send(f'You are {gay}% gay')

@client.command()
@commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
async def ayayarsp(ctx, choice = None):
    if choice == None:
        await ctx.send('Please give a choice! (Rock, Paper, Scissors)')
    else :
        choice.lower()
    user = ctx.message.author.name
    choices = ["rock", "paper", "scissors"]
    computer = choices[random.randint(0,2)]
    if choice == computer:
        await ctx.send(f'{user} used {choice}')
        await ctx.send(f'While Ayaya Ayaya used {computer}')
        await ctx.send("Tie!")
    elif choice == "scissors":
        if computer == "rock":
            await ctx.send(f'{user} used {choice}')
            await ctx.send(f'While Ayaya Ayaya used {computer}')
            await ctx.send("You Lost!")
        else:
            await ctx.send(f'{user} used {choice}')
            await ctx.send(f'While Ayaya Ayaya used {computer}')
            await ctx.send("You Won!")
    elif choice == "rock":
        if computer == "paper":
            await ctx.send(f'{user} used {choice}')
            await ctx.send(f'While Ayaya Ayaya used {computer}')
            await ctx.send("You Lost!")
        else:
            await ctx.send(f'{user} used {choice}')
            await ctx.send(f'While Ayaya Ayaya used {computer}')
            await ctx.send("You Won!")
    elif choice == "paper":
        if computer == "scissors":
            await ctx.send(f'{user} used {choice}')
            await ctx.send(f'While Ayaya Ayaya used {computer}')
            await ctx.send("You Lost!")
        else:
            await ctx.send(f'{user} used {choice}')
            await ctx.send(f'While Ayaya Ayaya used {computer}')
            await ctx.send("You Won!")
    else:
        await ctx.send("Use a valid choice")

@client.command(pass_context = True)
async def stop(ctx):
    print("Stop")
    global stop
    stop = True

client.run('NTkyMjgzMzA4MjcyOTEwMzM2.XQ9Feg.Jfd6ChqFwm84o6kCMkat6yAK0SM')
