import discord
import re
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import math
Client = discord.Client()

@Client.event
async def on_ready():
        print("logged in as: ")
        print(Client.user.name)
        print("ID: ")
        print(Client.user.id)
        print("ready to use!")

@Client.event
async def on_message(message):
        if message.author == Client.user:
                return
        elif message.content == "!ping":
                await Client.send_message(message.channel,"pong!")
        elif message.content == "!":
                uid = str(message.author.id)
                x = str(random.randint(1,20))
                await Client.send_message(message.channel,'<@!'+uid+'>  ' + x)
        elif message.content == "!developer":
                await Client.send_message(message.channel,"Developer of this Bot is Gandalf. Here is my Discord server: https://discord.gg/3fnvP7z")
        elif message.content.startswith("(") and message.content.endswith(")"):
                uid = str(message.author.id)
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                if len(a) == 2:
                        rolls = []
                        sumrolls = 0
                        while a[0] != 0:
                                x = random.randint(1,a[1])
                                sumrolls += x
                                rolls.append(x)
                                a[0] -= 1
                        if len(rolls) > 1:
                                rollsstr = "+".join(str(x) for x in rolls)+" = " + str(sumrolls)
                        else:
                                rollsstr = "+".join(str(x) for x in rolls)
                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                elif len(a) == 3:
                        if '+' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                rolls.append(mod)
                                sumrolls += mod
                                rollsstr = "+".join(str(x) for x in rolls)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '-' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls -= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"-"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '*' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls *= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"*"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '/' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls /= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"/"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
        elif message.content.startswith("!"):
                uid = str(message.author.id)
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                value1 = a[0]
                o = 3
                if len(a) == 4:
                        value2 = a[1]
                        value3 = a[2]
                        value4 = a[3]
                        checkfor1 = 0
                        checkfor20 = 0
                        rolls = []
                        while o != 0:
                                x = random.randint(1,20)
                                rolls.append(x)
                                if x == 1:
                                        checkfor1 += 1
                                elif x == 20:
                                        checkfor20 += 1
                                o -= 1
                        roll1 = rolls[0]
                        roll2 = rolls[1]
                        roll3 = rolls[2]
                        while roll1 > value1:
                                value4 -= 1
                                roll1 -= 1
                        while roll2 > value2:
                                value4 -= 1
                                roll2 -= 1
                        while roll3 > value3:
                                value4 -= 1
                                roll3 -= 1
                        rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==>"+" Misslungen!"
                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                        if checkfor1 == 2 or checkfor1 == 3:
                                rollsstrc = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " ==> KRITISCHER ERFOLG!"
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrc)
                        elif checkfor20 == 2 or checkfor20 == 3:
                                rollsstrb = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " ==> PATZER!"
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrb)
                        elif value4 == 0:
                                qualitylevel1 = 1
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrs)
                        elif value4 > 0:
                                await Client.send_message(message.channel,  '<@!'+uid+'>  ' + rollsstrs)
                        elif value4 < 0:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)

                elif len(a) == 1:
                        uid = str(message.author.id)
                        rolls = []
                        x = random.randint(1,20)
                        checkfor1 = 0
                        checkfor20 = 0
                        m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen!"
                        m_failure = "Du hast gewürfelt: "+str(x)+" ==> Misslungen!"
                        if x < a[0] and x != 1:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                        elif x == a[0]:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                        elif x > a[0]and x!= 20:
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                        elif x == 20:
                                rolls.append(x)
                                x = random.randint(1,20)
                                rolls.append(x)
                                if  x > a[0]:
                                        rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                else:
                                        rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigt)"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif x == 1:
                                rolls.append(x)
                                x = random.randint(1,20)
                                rolls.append(x)
                                if  x < a[0]:
                                        rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Kritischer Erfolg bestätigen: " +str(rolls[1])+ " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                else:
                                        rollsstr= "Du hast gewürfelt: "+str(rolls[0])+" Kritischer Erfolg bestätigen: "+str(rolls[1])+" ==> Gelungen(Kritischer Erfolg nicht bestätigt)"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                elif len(a) == 5:
                        uid = str(message.author.id)
                        if '-' in message.content:
                                value4 = a[3] + a[4]
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > a[0]:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > a[1]:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > a[2]:
                                        value4 -= 1
                                        roll3 -= 1
                                if value4 > a[3]:
                                        value4 = a[3]
                                else:
                                        value4 = value4
                                rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==>"+" Misslungen!!"
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)
                        elif '+' in message.content:
                                value4 = a[3] - a[4]
                                if value4 < 0:
                                        a[0] = a[0] + value4
                                        a[1] = a[1] + value4
                                        a[2] = a[2] + value4
                                        value4 = 0
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > a[0]:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > a[1]:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > a[2]:
                                        value4 -= 1
                                        roll3 -= 1
                                qualitylevel = value4/3
                                qualitylevel1 = math.ceil(qualitylevel)
                                rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Misslungen!"
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)
                        else:
                                value4 = a[3] - a[4]
                                if value4 < 0:
                                        a[0] = a[0] + value4
                                        a[1] = a[1] + value4
                                        a[2] = a[2] + value4
                                        value4 = 0
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > a[0]:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > a[1]:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > a[2]:
                                        value4 -= 1
                                        roll3 -= 1
                                qualitylevel = value4/3
                                qualitylevel1 = math.ceil(qualitylevel)
                                rollsstrf = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Misslungen!"
                                rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> KRITISCHER ERFOLG!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Du hast gewürfelt: " + ",".join(str(x) for x in rolls) + " ==> PATZER!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Du hast gewürfelt: " + ", ".join(str(x) for x in rolls) + " \nP*: " + str(value4) + " ==> Gelungen!"
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstrf)

                elif len(a) == 2:
                        if '-' in message.content:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] + a[1]
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen!"
                                m_failure = "Your roll: "+str(x)+" ==> Misslungen!"
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigt)"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                elif x == 1:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x < a[0]:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Auf kritischen Erfolg überprüfen: " +str(rolls[1])+ " ==> KRITISCHER ERFOLG!"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Auf kritischen Erfolg überorüfen: "+str(rolls[1])+" ==> Gelungen(Kritischer Erfolg nicht bestätigt)"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        elif '+' in message.content:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] - a[1]
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen!"
                                m_failure = "Du hast gewürfelt: "+str(x)+" ==> Misslungen!"
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigen)"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                        else:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] - a[1]
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Du hast gewürfelt: "+str(x)+" ==> Gelungen!"
                                m_failure = "Du hast gewürfelt: "+str(x)+" ==> Misslungen!"
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, '<@!'+uid+'>  ' + m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Patzer bestätigen: " +str(rolls[1])+ " ==> PATZER"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Patzer bestätigen: "+str(rolls[1])+" ==> Misslungen(Patzer nicht bestätigt"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                elif x == 1:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x < a[0]:
                                                rollsstr= "Du hast gewürfelt: " +str(rolls[0])+ " Auf kritischen Erfolg überprüfen: " +str(rolls[1])+ " ==> KRITISCHER ERFOLG!"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
                                        else:
                                                rollsstr="Du hast gewürfelt: "+str(rolls[0])+" Auf kritischen Erfolg überprüfen: "+str(rolls[1])+" ==> Gelungen"
                                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + rollsstr)
        elif message.content.startswith('*'):
                uid = str(message.author.id)
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                if len(message.content) in range(2,4):
                        x = random.randint(1,100)
                        hard1 = a[0]/2
                        hard = math.ceil(hard1)
                        crit1 = a[0]/5
                        crit = math.ceil(crit1)
                        if x < crit or x == crit:
                                 answer = "Your roll: "+str(x)+" ==> CRITICAL SUCCESS"
                                 await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
                        elif x < hard or x == crit:
                                answer = "Your roll: "+str(x)+" ==> HARD SUCCESS"
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
                        elif x < a[0] or x == a[0]:
                                answer = "Your roll: "+str(x)+" ==> SUCCESS"
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
                        elif x >a[0]:
                                answer = "Your roll: "+str(x)+" ==> Failed"
                                await Client.send_message(message.channel, '<@!'+uid+'>  ' + answer)
        elif message.content.startswith('+'):
                a = [int(num) for num in re.findall(r"\d+", '<@!'+uid+'>  ' + message.content)]
                rolls = []
                successcount = 0
                botchcount = 0
                botchcheck = a[0]/2
                while a[0] != 0:
                        x = random.randint(1,6)
                        rolls.append(x)
                        if x == 5 or x == 6:
                                successcount += 1
                        elif x == 1:
                               botchcount += 1
                        a[0] -= 1
                answer = "Your rolls: "+",".join(str(x) for x in rolls)+" ==> "+str(successcount)+" success(es)"
                if botchcount < botchcheck:
                        await Client.send_message(message.channel,answer)
                elif botchcount > botchcheck and successcount == 0:
                        answer = "Your rolls: "+",".join(str(x) for x in rolls)+" ==> CRITICAL BOTCH!"
                        await Client.send_message(message.channel,answer)
                elif botchcount > botchcheck:
                        answer = "Your rolls: "+",".join(str(x) for x in rolls)+" ==> BOTCH! "+str(successcount)+" success(es)"
                        await Client.send_message(message.channel,answer)

        elif message.content == '%help' :
                await Client.send_message(message.channel, "Common Commands: \n -`(<how many dices?>d<how many sides>)` lets you roll various dices. you can even add, multiply, subtract, or divide a number from the sum of all dices. EXAMPLE: (3d6+5) \n - `!` rolls 1d20 \n\n The Dark eye Commands:\n\n- `!<attribute>` lets you roll for a specific attribute. You can even add a modifier. EXAMPLE: !13,+2 \n- `!<attribute>,<attribute>,<attribute>,<skill value>` lets you roll for a Skill. You can even add a modifier. EXAMPLE: !13,14,13,5,-3 \n\nCall of Cthulhu Commands:\n\n- `*<Skill>` lets you roll for a skill. EXAMPLE: *50")
        elif message.content == 'zone':
                x = random.randint(1,20)
                if x == 1 or x == 3 or x == 5:
                        zone = str(x)+": linkes Bein \nErste und zweite Wunde: AT, PA, GE, INI-Basis -2, GS -1 \nDritte Wunde: Sturz, kampfunfähig"
                elif x == 2 or x == 4 or x == 6:
                        zone = str(x)+": rechtes Bein \nErste und zweite Wunde: AT, PA, GE, INI-Basis -2, GS -1 \nDritte Wunde: Sturz, kampfunfähig"
                elif x in range(7,8):
                        zone = str(x)+": Bauch \nErste und zweite Wunde: AT, PA, KO, KK, GS, INI-Basis -1, 1W6 TP \nDritte Wunde: Bewusstlos, Blutverlust"
                elif x == 9 or x == 11 or x == 13:
                        zone = str(x)+": linker Arm: \nErste und zweite Wunde: AT, PA, KK, FF -2 mit diesem Arm \nDritte Wunde: Arm handlungsunfähig"
                elif x == 10 or x == 12 or x == 14:
                        zone = str(x)+": rechter Arm: \nErste und zweite Wunde: AT, PA, KK, FF -2 mit diesem Arm \nDritte Wunde: Arm handlungsunfähig"
                elif x in range(15,18):
                        zone = str(x)+": Brust: \nErste und zweite Wunde: AT, PA, KO, KK -1, 1W6 TP \nDritte Wunde: bewusstlos, Blutverlust"
                elif x == 19 or x == 20:
                        zone = str(x)+": Kopf: \nEste und zweite Wunde: MU, KL, IN, INI-Basis -2, INI -2w6 \nDritte Wunde: 2W6 TP, Blutverlust"
                await Client.send_message(message.channel, zone)
        elif message.content == 'patzer':
                x = random.randint(1,6)
                y = random.randint(1,6)
                result = x + y
                if result == 2:
                        patzer = str(result)+": Waffe zerstört! \nINI -4 wegen Desorientierung; Hat die Waffe einen BF 0 oder weniger, so wird das Ergebnis als 'Waffe verloren' gewertet und der BF der Waffe steigt um 2; Greift man mit der Faust an, gilt dieses Ergebnis als 'schwerer Eigentreffer'"
                elif result in range(3,5):
                        patzer = str(result)+": Sturz! \nDer Patzende liegt auf dem Boden und bekommt dementsprechend erschwernisse(WdS S. 57), bis er wieder aufstehen kann. Dies benötigt eine Aktion Position und eine um seine BE erschwerte GE-Probe. Ein Held mit SF Standfest oder dem Vorteil Balance kann einen Sturz in ein Stolpern umwandeln wenn ihm eine GE-Probe(Standfest: +2, Balance: +-0, herausragende Balance: -4), die um die BE erschwert ist, gelingt. INI -2 wegen Desorientierung."
                elif result in range(6,8):
                        patzer = str(result)+": Stolpern! \nINI -2 wegen Desorientierung"
                elif result in range(9,10):
                        patzer = str(result)+": Waffe verloren! \nDer Patzende muss in der folgenden Runde die Aktion Position aufwenden, um eine GE-Probe abzulegen, bei deren gelingen er an seine Waffe gelangt; oder aber er wechselt die Waffe oder flieht. Handelt es sich bei der Waffe um Fäuste und Füsse, so wird das Ergebnis als Sturz gewertet. INI -2 wegen Desorientierung."
                elif result == 11:
                        patzer = str(result)+": An eigener Waffe verletzt! \nDer betroffene erleidet Waffenschaden durch eigene Waffe(TP auswürfeln; keine zusätzlichen TP aus hoher KK oder Ansagen) und eventuell sogar eine Wunde (bei mehr als KO/2 SP) mit den dort genannten Folgen; INI -3 wegen Desorientierung."
                elif result == 12:
                        patzer = str(result)+": Schwerer Eigentreffer! \nINI -4. Der Betroffene erleidet schweren Schaden durch eigene Waffe(TP auswürfeln und verdoppeln; keine zusätzlichen TP aus hoher KK oder Ansagen) und eventuell sogar eine Wunde(bei mehr als KO/2 SP) mit den dort genannten Folgen; INI -4 wegen Desorientierung."
                await Client.send_message(message.channel, patzer)



Client.run("NjAwMjc5MDQ4MTkwNjg5MzAw.XSxb3w.NhEWKjwcCzKKfknqhXCR0zpQAdU")
