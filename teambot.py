import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import os
import sys

slrb_token = os.environ['slrb_token']

client = commands.Bot(command_prefix='!!')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(sys.version)
    print(discord.__version__)




@client.command()
async def rect(ctx):
    # メンバーカウント
    cnt = int(6)
    cnt2 = int(6)
    cnt3 = int(6)
    cnt4 = int(6)
    cnt5 = int(6)
    # パテメン配列
    partyOne = ["name"]
    partyTwo = ['name']
    partyThree = ['name']
    partyFour = ['name']
    partyFive = ['name']
    # 初期Embed
    test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
    test.add_field(name="----------------", value="パーティー１",inline=False)
    test.add_field(name="----------------", value="パーティー2",inline=False)
    test.add_field(name="----------------", value="パーティー3",inline=False)
    test.add_field(name="----------------", value="パーティー4",inline=False)
    test.add_field(name="----------------", value="パーティー5",inline=False)
    msg = await ctx.send(embed=test)
    #投票のemoji
    await msg.add_reaction('1️⃣')
    
    await msg.add_reaction('2️⃣')
    
    await msg.add_reaction('3️⃣')
    
    await msg.add_reaction('4️⃣')
    
    await msg.add_reaction('5️⃣')
    



    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:
            pass
        else:
            return emoji == '1️⃣' or emoji == '2️⃣' or emoji == '3️⃣' or emoji == '4️⃣' or emoji == '5️⃣'

    while True:
        reaction, user = await client.wait_for('reaction_add',check=check)
        print(str(reaction.emoji))
        # 追加
        if str(reaction.emoji) == '1️⃣':
            if user.name in partyOne:
                partyOne.remove(user.name)
                cnt += 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
            else:
                partyOne.append(user.name)
                cnt -= 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
        elif str(reaction.emoji) == '2️⃣':
            if user.name in partyTwo:
                partyTwo.remove(user.name)
                cnt2 += 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
            else:
                partyTwo.append(user.name)
                cnt2 -= 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
        elif str(reaction.emoji) == '3️⃣':
            if user.name in partyThree:
                partyThree.remove(user.name)
                cnt3 += 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
            else:
                partyThree.append(user.name)
                cnt3 -= 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
        elif str(reaction.emoji) == '4️⃣':
            if user.name in partyFour:
                partyFour.remove(user.name)
                cnt4 += 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
            else:
                partyFour.append(user.name)
                cnt4 -= 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
        elif str(reaction.emoji) == '5️⃣':
            if user.name in partyFive:
                partyFive.remove(user.name)
                cnt5 += 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
            else:
                partyFive.append(user.name)
                cnt5 -= 1
                test = discord.Embed(title='現在のパーティー編成',color=0x1e90ff)
                test.add_field(name="----------------", value="パーティー１",inline=False)
                test.add_field(name=f"あと__{cnt}__人募集中",value='\n'.join(partyOne), inline=False)
                test.add_field(name="----------------", value="パーティー2",inline=False)
                test.add_field(name=f"あと__{cnt2}__人募集中",value='\n'.join(partyTwo), inline=False)
                test.add_field(name="----------------", value="パーティー3",inline=False)
                test.add_field(name=f"あと__{cnt3}__人募集中",value='\n'.join(partyThree), inline=False)
                test.add_field(name="----------------", value="パーティー4",inline=False)
                test.add_field(name=f"あと__{cnt4}__人募集中",value='\n'.join(partyFour), inline=False)
                test.add_field(name="----------------", value="パーティー5",inline=False)
                test.add_field(name=f"あと__{cnt5}__人募集中",value='\n'.join(partyFive), inline=False)
                await msg.edit(embed=test)
        # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
        await msg.remove_reaction(str(reaction.emoji), user)



# Botの起動とDiscordサーバーへの接続
client.run(slrb_token)
