import discord #導入discord
import os

bot = discord.Bot(intents = discord.Intents.all()) 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "介紹這裡": 
        await message.channel.send("這裡是咪咪樂園，你好~我是柯基管家!") 
    if message.content == "法規": 
        await message.channel.send("咪咪樂園法規除了不能說「你媽」、「黑人大雞巴」和不能po色色其他都沒有限制!咪咪樂園歡迎你~") 
    if message.content.startswith("你媽"): 
        await message.channel.send("又在你媽，你是不是子寧阿?腦殘!") 
    if message.content.startswith("黑人大雞"): 
     await message.channel.send("黑你媽，你再黑~眼睛會跟老二位置對調!") 
    if message.content.startswith("黑人"): 
     await message.channel.send("又要黑人大雞巴了嗎?董昱安?") 
    if message.content.startswith("大雞"): 
     await message.channel.send("別再大雞巴了拉，臭黑人")
    if message.content.startswith('說'):
      tmp = message.content.split(" ",2)
    if len(tmp) == 1:
     await message.channel.send("你要我說什麼啦？")
    else:
     await message.channel.send(tmp[1])

@bot.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.watching,  # 設定狀態
        name="裸猿們的低端操作" ) # 這定自訂義狀態
    await bot.change_presence(activity=activity)
    print(f"「{bot.user}」已登入")


bot.run(os.environ['bot_token']) #運行機器人