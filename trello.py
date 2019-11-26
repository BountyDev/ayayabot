import discord
import random
import json
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

async def number_organizer():
    with open('tasks.json') as f:
            tasks = json.load(f)
    tsk = {}
    tsknum = 1
    number = 1
    while number < 1+len(tasks):
        num = str(number)
        if tasks[num] != None:
            tsk[tsknum] = task[num]
            tsknum+=1
        number+=1
    with open('tasks.json', 'w+') as f:
        tasks = json.dump(tsk, f)



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("tasking stuff"))
    print("ONLINE")

@client.command(pass_context = True)
async def addtask(ctx, task = None, section = None, importance = None):
    if task == None:
        await ctx.send("**Missing parameters !addtask <name> <section> <importance>**")
    elif section == None:
        await ctx.send("**Missing parameters !add_task <name> <section> <importance>**")
    elif importance == None:
        await ctx.send("**Missing parameters !add_task <name> <section> <importance>**")
    elif 6 < int(importance) > 0:
        await ctx.send("**Importance should be a number 0-5, 0 for completed and 1-5 for its importance level**")
    else:
        try:
            with open('tasks.json') as f:
                tasks = json.load(f)
        except FileNotFoundError:
            print("Could not load amounts.json")
            tasks = {}
        tasks[len(tasks)+1] = importance + "_" + task + "_" + section

        with open('tasks.json', 'w+') as f:
            taskadd = json.dump(tasks, f)
            await ctx.send(f"**You've added {task} into {section}**")
        with open('tasks.json') as f:
            tasks = json.load(f)

@client.command(pass_context = True)
async def edittask(ctx, task = None, sel = None, val = None):
    if task != None:
        if sel != None:
            if val != None:
                with open('tasks.json') as f:
                    tasks = json.load(f)
                number = 1
                while number < len(tasks):
                    num = str(number)
                    curtask = tasks[num].split("_")[1]
                    curimp = tasks[num].split("_")[0]
                    cursect = tasks[num].split("_")[2]
                    if curtask == task:
                        if sel == "importance":
                            if isinstance(s, int):
                                tasks[num] = val + "_" + curtask + "_" + cursect
                                await ctx.send(f"**You've changed {curimp} to {val}**")
                            else:
                                await ctx.send("Pick a number between 1-5")
                        elif sel == "name":
                            tasks[num] = curimp + "_" + val + "_" + cursect
                            await ctx.send(f"**You've changed {curtask} to {val}**")
                        elif sel == "section":
                            tasks[num] = curimp + "_" + curtask + "_" + val
                            await ctx.send(f"**You've changed {cursect} to {val}**")
                        else:
                            await ctx.send("**Please pick a valid value (importance)(name)(section)**")
                        with open('tasks.json', 'w+') as f:
                            tasks = json.dump(tasks, f)
                    number+=1
            else:
                await ctx.send("**Missing parameters !edittask <name> <what you want to edit(importance,name,section)> <new value>**")
        else:
            await ctx.send("**Missing parameters !edittask <name> <what you want to edit(importance,name,section)> <new value>**")
    else:
        await ctx.send("**Missing parameters !edittask <name> <what you want to edit(importance,name,section)> <new value>**")


@client.command(pass_contet = True)
async def gettask(ctx, task = None):
    with open('tasks.json') as f:
        tasks = json.load(f)
    number = 1
    while number < 1+len(tasks):
        num = str(number)
        curtask = tasks[num].split("_")[1]
        if curtask == task:
            curimport = tasks[num].split("_")[0]
            cursection = tasks[num].split("_")[2]
            embed = discord.Embed(title="Task", description=curtask, color=0x00ff00)
            embed.add_field(name="Importance", value=curimport, inline=False)
            embed.add_field(name="Section", value=cursection, inline=False)
            await ctx.send(embed=embed)
        number+=1

@client.command(pass_context = True)
async def list(ctx):
    with open('tasks.json') as f:
        tasks = json.load(f)
    number = 1
    embed = discord.Embed(title="Tasks", description="List of tasks", color=0x00ff00)
    while number < 1+len(tasks):
        num = str(number)
        curtask = tasks[num].split("_")[1]
        curimport = tasks[num].split("_")[0]
        cursection = tasks[num].split("_")[2]
        embed = discord.Embed(title="Task", description=curtask, color=0x00ff00)
        embed.add_field(name="Importance", value=curimport, inline=False)
        embed.add_field(name="Section", value=cursection, inline=False)
        await ctx.send(embed=embed)
        number+=1

@client.command(pass_context = True)
async def removetask(ctx, task = None):
    with open('tasks.json') as f:
        tasks = json.load(f)
    number = 1
    tsk = {}
    tsknum = 1
    while number < 1+len(tasks):
        num = str(number)
        curtask = tasks[num].split("_")[1]
        if curtask != task:
            tsk[tsknum] = tasks[num]
            tsknum+=1
        else:
            cursection = tasks[num].split("_")[2]
            await ctx.send(f"**You've deleted {curtask} from {cursection}**")
        number+=1
    with open('tasks.json', 'w+') as f:
        tasks = json.dump(tsk, f)




client.run("NjA1MTg3NDk2MzE3Mjg4NDUw.XT43Qg.yeBaBJHBy-wqI0CI5fdkTF3JFIk")
