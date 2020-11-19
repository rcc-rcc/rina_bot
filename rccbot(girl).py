import discord
from discord.ext import commands
import time
import random
import asyncio
import datetime



#オブジェ★
bot = commands.Bot(command_prefix='Rb.')

client = discord.Client()
#起動するときの処理
@bot.event
async def on_ready():
    print('___________')
    print('kami kidou')
    print(bot.user.name)
    print(bot.user.id)
    print('___________')

#ふはは



#message処理
@bot.command()
async def id(ctx):
    await ctx.send(ctx.author.id)

#google
@bot.command()
async def google(ctx):
    await ctx.send('https://www.google.com/')

#google検索
@bot.command()
async def Google(ctx,*,te):
    await ctx.send("https://www.google.com/search?client=firefox-b-d&q="+te)

#yahoo
@bot.command()
async def yahoo(ctx):
    await ctx.send('https://www.yahoo.co.jp/')

#yahoo検索
@bot.command()
async def Yahoo(ctx,*,te):
    await ctx.send("https://search.yahoo.co.jp/search?p="
    +te+
    "&aq=-1&oq=&ai=3jBr9iyPTjiW84ZgbnZ0mA&ts=7167&ei=UTF-8&fr=top_ga1_sa&x=wrt"
    )

#chaina
@bot.command()
async def china(ctx):
    await ctx.send('https://www.baidu.com/')

#chana検索
@bot.command()
async def China(ctx,*,te):
    await ctx.send("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="
    +te+
    "&oq=twitter&rsv_pq=e5f1e3af00247199&rsv_t=7e8635s%2FGtLgDg3TTQs3uFOsCciUiDz2RjcH0K1Zr5%2FDj9Y4UsSrvHv7y7U&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=6636&rsv_sug3=29&rsv_sug1=15&rsv_sug7=101&rsv_sug2=0&rsv_sug4=7363&rsv_sug=1")

#twitter
@bot.command()
async def twitter(ctx):
    await ctx.send('https://twitter.com')

#twitter検索
@bot.command()
async def Twitter(ctx,*,te):
    await ctx.send("https://twitter.com/search?q="+te+"&src=typd")

#youtbe
@bot.command()
async def youtube(ctx):
    await ctx.send('https://www.youtube.com/')

#YouTube検索
@bot.command()
async def Youtube(ctx,*,te):
    await ctx.send("https://www.youtube.com/results?search_query="+te)

#niconico623829061042700308
@bot.command()
async def niconico(ctx):
    await ctx.send('https://www.nicovideo.jp/')

#noconico検索
@bot.command()
async def NicoNico(ctx,*,te):
    await ctx.send("https://www.nicovideo.jp/search/"+te+"?f_range=0&l_range=0&opt_md=&start=&end=")

#マミーのコールコマンド
@bot.command()
async def マミー(ctx):
    await ctx.send(ctx.author.mention + 
    '''
    くん❣のんでなくない？
    ''')
    time.sleep(0.5)
    await ctx.send('うぉううぉう❣❣')
    time.sleep(1.5)
    await ctx.send('あマミーを片手に')
    time.sleep(1.5)
    await ctx.send('グイッグイッグイグイ！')
    time.sleep(1.5)
    await ctx.send('マミーを飲んで！')
    time.sleep(1.5)
    await ctx.send('マミーの中には')
    time.sleep(1)
    nyu = await ctx.send("にゅ")
    await nyu.edit(content="乳")
    time.sleep(0.2)
    san = await ctx.send("さん")
    await san.edit(content="酸")
    time.sleep(0.2)
    kin = await ctx.send(content="きん")
    await kin.edit(content="菌")
    time.sleep(1.5)
    await ctx.send('体にいいね！')
    time.sleep(1)
    nyu = await ctx.send("にゅ")
    await nyu.edit(content="乳")
    time.sleep(0.2)
    san = await ctx.send("さん")
    await san.edit(content="酸")
    time.sleep(0.2)
    kin = await ctx.send(content="きん")
    await kin.edit(content="菌")
    time.sleep(1.2)
    await ctx.send('いつも心に！')
    nyu = await ctx.send("にゅ")
    await nyu.edit(content="乳")
    time.sleep(0.2)
    san = await ctx.send("さん")
    await san.edit(content="酸")
    time.sleep(1)
    kin = await ctx.send(content="きん")
    await kin.edit(content="菌")
    time.sleep(1.5)
    await ctx.send('最高の飲み物❣')
    time.sleep(1.5)
    await ctx.send('その名は？')
    time.sleep(0.5)
    await ctx.send('マミー')
    
#乱数
@bot.command()
async def 乱数(ctx):
    r = random.randint(0, 100)
    await ctx.send(r)

#世界で一番最強になれます
@bot.command()
async def この世で一番最強なのは(ctx): 
    await ctx.send(ctx.author.display_name +"さんだと思います❣❣")

#ピンやって！
@bot.command()
async def ping(ctx):
    st = time.time()
    m = await ctx.send("計測中")
    await m.edit(content=f"{round(time.time()-st,3)*1000}msでした.")

#オウム返し
@bot.command()
async def オウム返し(ctx,*,te):
    await ctx.send(te)


#質問
@bot.command()
async def 質問(ctx,*,te):
    embed = discord.Embed(title="質問", description="ボット作成者レックに質問を投げつけます", color=0xe32bd1)
    embed.add_field(name=ctx.author.display_name +"さんからの質問です", value=te)

    await ctx.send(embed=embed)




#ゲームコマンド
#おみくじ
@bot.command()
async def おみくじ(ctx):
    kuzi = random.choice(['大凶','凶','末吉','吉','小吉','中吉','大吉','神吉'])
    await ctx.send(kuzi)
    print (kuzi)

#ランダムパティー組みたい()
@bot.command()
async def p(ctx):
    kuzi = random.choice(['大凶','凶','末吉','吉','小吉','中吉','大吉','神吉'])
    await ctx.send(kuzi)
    print (kuzi)






#プログラムを持久走させる
bot.run('NjIwNTI0MzA5MTc3MzAzMDQw.XXYCTA.CBXGx6Ou69Lbapj15o6SvDoai_8')