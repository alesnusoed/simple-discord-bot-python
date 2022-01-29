from discord.ext import commands
import discord

client = commands.Bot(command_prefix = '')

@client.event

async def on_ready():

  print('negr rabotat')
  await client.change_presence(status=discord.Status.idle,activity=discord.Game('Brawl Stars'))

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx,member:discord.Member, *, reason='Наверное ты и сам догадываешься'):
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(f'нарушителей мы не любим{ member.mention }')

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'карыч сегодня добрый , он простил {user.mention}')
        return





bad_words = ['гей','пидр','еблан','бот хуйня','ты еблан']



@client.event

async def on_message( message):

  await client.process_commands( message)


  msg = message.content.lower() 


  if msg in bad_words:

    await message.delete()

    await message.author.send(f'{message.author.name},еще раз это услышу выебу на месте')

@client.command()
async def чистка(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount))
    await ctx.channel.send(':: Сообщения успешно удалены')

@client.event

async def on_ready():

  print('negr rabotat')

@client.command()
@commands.has_permissions(administrator=True)
async def кик(ctx, member: discord.Member, *, reason='Гнев КАрыча'):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f'КАРЫЧ наказал игрока -> { member.mention }')

@client.command()

async def тест(ctx):

  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")
  await ctx.reply(f"{ctx.author.mention} да  ")
  await ctx.reply(f"{ctx.author.mention} нет  ")
  await ctx.reply(f"{ctx.author.mention} возможно  ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} отрицаю ")
  await ctx.reply(f"{ctx.author.mention} предпологаю  ")


@client.command()

async def ua(ctx):

  await ctx.reply(f"{ctx.author.mention} https://vshkole.com/ ")


@client.command()

async def говно(ctx):

  await ctx.reply(f"{ctx.author.mention} https://tenor.com/view/wow-social-credit-gone-omg-gif-23106506")


@client.command()

async def ru (ctx):

  await ctx.reply(f"{ctx.author.mention} https://gdz.ru/ ")


@client.command()

async def Ку(ctx):

  await ctx.reply(f"{ctx.author.mention} привет")


@client.command()

async def фотографирую_закат(ctx):

  await ctx.reply(f"{ctx.author.mention} Фотографирую закат, будто пару лет назад Без тебя, без тебя, без тебя Фотографирую закат, будто пару лет назад Без тебя, без тебя, без тебя Уйди, в моем сердце свечи гаснут, становлюсь холодным  Молчи, все не вечно, все не важно, я умру свободным Я не вижу лиц, я вижу твое нутро И среди него мне не нравится ничего Просто прекрати пос-пос-посещать мои ебаные сны Фотографирую закат, будто пару лет назад Без тебя, без тебя, без тебя Фотографирую закат, будто пару лет назад Без тебя, без тебя, без тебя Все те лица, что запечатлил Лишнее место, пора удалить Думаю, что я остался один Уже никогда не останусь один Уйди, в моем сердце свечи гаснут, становлюсь холодным Молчи, все не вечно, все не важно, я умру свободным Я не вижу лиц, я вижу твое нутро И среди него мне не нравится ничего Просто прекрати пос-пос-посещать мои ебаные сны Фотографирую закат, будто пару лет назад Без тебя, без тебя, без тебя Фотографирую закат, будто пару лет назадБез тебя, без тебя, без тебя")


@client.command()

async def цитата(ctx):

  await ctx.reply(f"{ctx.author.mention} Я слишком много хуйни говорил чтоб что то выбрать.jirzy#2730")


@client.command()

async def история_Василечка(ctx):

  await ctx.reply(f"{ctx.author.mention}  вот он... https://tenor.com/view/%D0%BA%D0%B0%D1%80%D0%BA%D0%B0%D1%80%D1%8B%D1%87-gif-24527932")


@client.command()

async def GYM(ctx):

  await ctx.reply(f"{ctx.author.mention} https://tenor.com/view/van-darkholme-gachimuchi-gachi-foo-woo-gif-20020200")


@client.command()

async def гуль(ctx):

  await ctx.reply(f"{ctx.author.mention}У меня нет проблем, кроме моей башки1000-7, я умер, прости Этот долбаный  дождь нагоняет тоски 1000-7, я умер, прости И им всем никогда меня не победить 1000-7, я уже погиб У меня есть суммы, но мне так по-о-о-х Не вывожу из зо рта, пох Я чувствую вкус крови на губах, сдох Им никогда не победить меня (Никогда) Под её окном написал «Ты боба»Клонит но только если под утро Это мёртвый звук на колени боба  Я реально мёртвый и это — не шутка У меня нет проблем, кроме моей башки 1000-7, я умер, прости Этот долбаный дождь нагоняет тоски 1000-7, я умер, прости Им всем никогда меня не победить 1000-7, я уже погиб У меня нет проблем, кроме моей башки 1000-7, я умер, прости Этот долбаный дождь нагоняет тоски 1000-7, я умер, прости Им всем никогда меня не победить 1000-7, я уже погиб У меня есть суммы, но мне так по-о-о-х Не вывожу из зо  рта, пох Я чувствую вкус крови на губах, сдох Им никогда не победить меня (Никогда) https://tenor.com/view/tokyo-ghoul-creepy-look-at-me-gif-13488832")


@client.command()

async def скала2(ctx):

  await ctx.reply(" https://tenor.com/view/van-darkholme-what-gif-24334428")

@client.command()
async def команды(ctx):
  embed = discord.Embed(title ="команды", colour=discord.Color.orange()) # В color можно поменять цвет таблице.
  embed.add_field(name="команды", value="список всего,что есть в этом боте") # Можно сколько угодно строк вставить.
  embed.add_field(name="лист команд", value="дз,команды_людей,мемы,разрабы,сервера,модерация")
  await ctx.send(embed=embed) #





@client.command()

async def чт(ctx):

  await ctx.reply(f"{ctx.author.mention} https://tenor.com/view/see-it-like-final-hamster-scared-gif-14498643")

@client.command()

async def умный(ctx):

  await ctx.reply("с̵͙̥̝͎̍ӓ̸̢̛͙́͂́͒̽͑̀͂͝м̴͚͙̅̈́̀̅͑ы̸̝͖̤̱̃е̵̲̝̺̗͋̅͐̐̑͌̒̃͝ ̶̧̡̳̠̹̳̖́͐̈́̀̅͆̑̽̀у̶̢̯̼̲̱͖̇̿͆̂̀̑̒̏̇̆ͅͅм̵̙͂͆̋̑̚н̵̪͍̮̮̥̥͖̦͍̘̍͑̕ы̸̭͐͋͛͆̈̂̒ӗ̸̯̙͉͓̮͍̜̗͔͌̆̍̃̊͌̑̚ ̵̨͙̫̹̃͒̾͗̕ч̷̡̼͓̻͚̣̉̈́̀̌͛̈́͘͜е̵̢̡͚̖͈͂͗̄͘л̵͈͓̹͙̬̰̦̳̃̀̕͝ͅы̸̩͕̳̰̭̤̥̯͇́ ̷̥̙́̏э̸̧̖̘̠͍̥̜̠̐͊̈́т̵̩̞̫͗͐̂о̶̝͔͗̉͋ ̵̧͓̤͍̳̾̍̆̀̎̓̆̕͝о̶̙̮̘̐͒̃̏͆̔̕̚н̴̨̥͓̠̺̭̬̞̣̀̎͋͑͊и̷̩̟̅̏̇͋͝ ̷̡̧͚̬̘̘̥͚̽̊̅̌̃͒͝-̵̬̒́̈́̆̅̍̎͘͘ ̷̧͎͍͇̩͇͔͕̣̊-̴̢̭̯̯͎́̐͆̀̀̓ ̵͇͖͉̥̭̗̮̉͊̆͜≯̡̗̠̻̓̎ ̴͍̩̫̙̂̀̓̇к̴̧̮͙̳̝̦̙͖̦̎͊͒т̴͓̥͂о̷͙̭̇̇͌̿͛-̸̜̭͉̲̙͋̑̇̾̽͌̀̊̚т̴͍͋͛͛̾̈́ӧ̶̡̨̞̹́̆̎#̴̢̞́̅́̒̀͘8̵̢̨͔͍̰͎͆̇̄́̀ͅ1̸̢̛̼̮̣͖̹̫͔͖̮̿̇͐̏̎̏̉͠7̷̢͇͈͐̈̓͗͂̿̓̚͠0̷̡̹͈̟̗̻̘̗͕̘́̃̏͗͆̍́,̸̙̔̐́́̇D̸̜͎̬̘͔͓̋̍͒͝Ữ̵̧̧̨̧͉͕͖͓̳͒̀D̷̫̺̘̣͍͒O̸̡̳͎̹̥͝ͅS̵̒̂̌̆̄̅̓͊̉͆ͅA̶̫̍̃̅̐̇̂̕ͅ#̷̡͔̣͔̖̀8̵̛̘͔̞̪͖̯̰͙̫9̶̨͓̪̦̻͖̉̀̍́̈́̒͑̈͑̓8̴̭̰͈̰̣̠̿0̸̝̳͈͓͔͚͚̹̈́̂́͑̈́̓͝,̶̬̗̻͇͖̮̿̊͆̅̉̎̈́̚͝G̸̥̍̂͑͝.̶̤̼͈̟̯̜̈̽̄̇P̴̛̛͓͍̮̺̜̪͔̤̱̿͗̈́͊.̵̧͈̇L̶̡̛̹̦̖̭̘͚̘͎͇̽̓́̿͋͠.̶̢̛̮̫͍̪̳͛̎̈̅͗̏̒̋̕͜-̴̢̯̰̮̱̬́̐͊͑̓͐͋ͅR̷̢̼̗̃̉̂̃̌̚U̶͎̝͕̯̟̞͂͛̒́̿̾͆͒͆͜S̴̢̛̫̈͋͐̉̑̎͑͘͝#̷̢̡̡̡͓̺͚͕̱͊͊͝1̴̗͍̯͙͉̹̠̭̽̊͛͐̏1̴̝̣͉͙̹̻͓̓͌͒̓̄͌̊̓͘ͅ6̷̧̛̻̖͚͓͚̆̓͊̂̀͑͌̕͝ͅ1̶̨̗̯̟̻̮͎̟̮̀͋̄͝")


@client.command()

async def скала_скример(ctx):

  await ctx.reply(f"{ctx.author.mention} https://tenor.com/view/the-rock-dwayne-johnson-dwayne-the-rock-tea-joe-moment-gif-22606108")



@client.command()

async def dudosa(ctx):

  await ctx.reply(f"{ctx.author.mention} сервер самого лучшего кодера которого я знаю https://discord.gg/Jk9RTVb66n")


@client.command()

async def memmny(ctx):

  await ctx.reply(f"{ctx.author.mention} https://discord.gg/HuZqqM8Esk")


@client.command()

async def sadle(ctx):

  await ctx.reply(f"{ctx.author.mention} https://discord.gg/HRXzrBxQzZ")



@client.command()
async def сервера(ctx):
  embed = discord.Embed(title ="команды", colour=discord.Color.orange()) # В color можно поменять цвет таблице.
  embed.add_field(name="список серверов", value="список серверов разработчик,друзей") # Можно сколько угодно строк вставить.
  embed.add_field(name="сервера", value="sadle,Dudosa,memmny,основной (канал потдержки)")
  await ctx.send(embed=embed) #

@client.command()

async def пошли_в_кровать_пупсик(ctx):

 await ctx.reply(f"{ctx.author.mention}пошли сладкий")

@client.command()

async def основной(ctx):

 await ctx.reply(f"{ctx.author.mention}https://discord.gg/axFsd6aY канал потдержки")






@client.command()
async def команды_людей(ctx):
  embed = discord.Embed(title ="команды", colour=discord.Color.orange()) # В color можно поменять цвет таблице.
  embed.add_field(name="пользовательские", value="список команд которые сделали ПОЛЬЗОВАТЕЛИ!") # Можно сколько угодно строк вставить.
  embed.add_field(name= "команд", value="питса,да,нет,го_в_рб,фотографирую_закат,мирш,финд,гей,цитата,история_Василечка")
  await ctx.send(embed=embed) #

@client.command()

async def финд(ctx):

 await ctx.reply(f"{ctx.author.mention}Я ещё несовершеннолетний, значит можно смотреть только детское")


@client.command()

async def харош(ctx):

 await ctx.reply(f"{ctx.author.mention}https://tenor.com/view/yes-good-gif-24371241")


@client.command()

async def твоя(ctx):

 await ctx.reply(f"{ctx.author.mention}нет твоя!")


@client.command()

async def го_в_рб(ctx):

 await ctx.reply(f"{ctx.author.mention}роблокс говно! ")


@client.command()

async def ку(ctx):

 await ctx.reply(f"{ctx.author.mention}привет!")



@client.command()

async def да(ctx):

 await ctx.reply(f"{ctx.author.mention}нет")


@client.command()

async def нет(ctx):

  await ctx.reply(f"{ctx.author.mention}пидора ответ")


@client.command()

async def скала(ctx):

  await ctx.reply(f"{ctx.author.mention}https://tenor.com/view/the-rock-the-rock-sus-the-rock-meme-tthe-rock-sus-meme-dwayne-johnson-gif-23805584")


@client.command()

async def питса(ctx):

 await ctx.reply(f"{ctx.author.mention}держи :pizza:")


@client.command()

async def гей(ctx):

 await ctx.reply(f"{ctx.author.mention}нет блин гавейн")


@client.command()

async def блять (ctx):

 await ctx.reply(f"{ctx.author.mention}**НЕ МАТЕРИСЬ СУКА**")


@client.command()

async def соси(ctx):

 await ctx.reply(f"{ctx.author.mention}***СОСЁТ*** (*захлебнулся и здох*)")




@client.command()
async def модерация(ctx):
  embed = discord.Embed(title ="команды", colour=discord.Color.blue()) # В color можно поменять цвет таблице.
  embed.add_field(name="модерация", value="команды,которые помогут с управлением сервера") # Можно сколько угодно строк вставить.
  embed.add_field(name="модерация", value="кодеры-***alexsnusoed#0457,DUDOSA#8980***                                                         ДИЗАЙНЕР-***sadle***  ")
  await ctx.send(embed=embed) 

@client.command()
async def разрабы(ctx):
  embed = discord.Embed(title ="команды", colour=discord.Color.gold()) # В color можно поменять цвет таблице.
  embed.add_field(name="разработчики", value="люди которые помогали делать этого бота..") # Можно сколько угодно строк вставить.
  embed.add_field(name="заработчики", value="(доступно если у бота есть права админа,и людям с ролью админ)                                                            **команды:чистка(кол.смс)**                                                                                                                                                                                **ban,unbane(бан,разбан участника)**")
  await ctx.send(embed=embed)




@client.command()
async def мемы(ctx):
  embed = discord.Embed(title ="команды", colour=discord.Color.red()) # В color можно поменять цвет таблице.
  embed.add_field(name="мемы", value="группа с мемыми гифками") # Можно сколько угодно строк вставить.
  embed.add_field(name="мемы", value="гачи-мучи(-GYM,-скала2),-харош(мем),-пошли_в_кровать_пупсик(для сладкого),ХАЛЯВА,но почему..,гуль,скала,скала_скример,чт,Куплинов,дед инсайд")
  await ctx.send(embed=embed) #


@client.command()
async def дз(ctx):
  embed = discord.Embed(title ="команды", colour=discord.Color.green()) # В color можно поменять цвет таблице.
  embed.add_field(name="дз", value="помощ с домашним заданием(гдз)") # Можно сколько угодно строк вставить.
  embed.add_field(name="дз", value="ru(гдз Росии), ua(гдз Украины)")
  await ctx.send(embed=embed) #

@client.command()

async def ХАЛЯВА(ctx):

  await ctx.reply(f"{ctx.author.mention} https://media.discordapp.net/attachments/653829227711430656/912338561871777792/KhVATAJ_BESPLATNO_Kega.gif ")




@client.command()

async def ладно(ctx):

  await ctx.reply(f"{ctx.author.mention} в трусах прохладно) ")
 

@client.command()

async def мирш(ctx):

 await ctx.reply(f"{ctx.author.mention}Ты обосрался, слижи блевоту")


@client.command()

async def я(ctx):

  await ctx.reply(f"{ctx.author.mention} а ")


@client.command()

async def э(ctx):

 await ctx.reply(f"{ctx.author.mention} ю ")


@client.command()

async def ы(ctx):

  await ctx.reply(f"{ctx.author.mention} ь")


@client.command()

async def щ (ctx):

  await ctx.reply(f"{ctx.author.mention} ъ ")


@client.command()

async def ч(ctx):

  await ctx.reply(f"{ctx.author.mention}ш ")


@client.command()

async def х(ctx):

  await ctx.reply(f"{ctx.author.mention} ц")

@client.command()

async def у(ctx):

  await ctx.reply(f"{ctx.author.mention}ф")


@client.command()

async def с(ctx):

  await ctx.reply(" т")


@client.command()

async def ф(ctx):

  await ctx.reply(f"{ctx.author.mention} х")


@client.command()

async def н(ctx):

  await ctx.reply(f"{ctx.author.mention}о")


@client.command()

async def л(ctx):

  await ctx.reply(f"{ctx.author.mention} м")


@client.command()

async def й(ctx):

 await ctx.reply(f"{ctx.author.mention} к")


@client.command()

async def з(ctx):

 await ctx.reply("и")


@client.command()

async def ё(ctx):

 await ctx.reply("ж")


@client.command()

async def д(ctx):

  await ctx.reply(f"{ctx.author.mention} е")


@client.command()

async def в(ctx):

  await ctx.reply(f"{ctx.author.mention} г)")


@client.command()

async def а(ctx):

 await ctx.reply(f"{ctx.author.mention}б")


@client.command()

async def б(ctx):

  await ctx.reply(f"{ctx.author.mention} в")


@client.command()

async def г(ctx):

  await ctx.reply(f"{ctx.author.mention} д")


@client.command()

async def е(ctx):

  await ctx.reply(f"{ctx.author.mention} ё")


@client.command()

async def ж(ctx):

  await ctx.reply(f"{ctx.author.mention} з")


@client.command()

async def и(ctx):

  await ctx.reply(f"{ctx.author.mention} й")


@client.command()

async def к(ctx):

  await ctx.reply(f"{ctx.author.mention} л")


@client.command()

async def м(ctx):

  await ctx.reply(f"{ctx.author.mention} н")


@client.command()

async def о(ctx):

  await ctx.reply(f"{ctx.author.mention} п")


@client.command()

async def р(ctx):

  await ctx.reply(f"{ctx.author.mention} с")


@client.command()

async def т(ctx):

  await ctx.reply(f"{ctx.author.mention} у")



@client.command()

async def пизда(ctx):

  await ctx.reply(f"{ctx.author.mention} твоя")


@client.command()

async def хай(ctx):

  await ctx.reply(f"{ctx.author.mention} привет")


@client.command()

async def hi(ctx):

  await ctx.reply(f"{ctx.author.mention} hello)")


@client.command()

async def бонжур(ctx):

  await ctx.reply(f"{ctx.author.mention} привет")


@client.command()

async def привет(ctx):

  await ctx.reply(f"{ctx.author.mention} привет")

@client.command()

async def чат(ctx):

  await ctx.reply(f"{ctx.author.mention}https://tenor.com/view/dead-chat-gif-23518284")

@client.command()

async def  но(ctx):

  await ctx.reply(f"{ctx.author.mention} https://tenor.com/view/dead-inside-cat-sad-sad-cat-sad-dead-inside-gray-cat-gif-24015090")

@client.command()

async def  Куплинов(ctx):

  await ctx.reply(f"{ctx.author.mention} https://tenor.com/view/%D0%BA%D1%83%D0%BF%D0%BB%D0%B8%D0%BD%D0%BE%D0%B2-%D1%88%D1%83%D1%82%D0%BA%D0%B0-%D0%B2%D1%88%D0%BE%D0%BA%D0%B5-weird-funny-face-gif-13299533")

@client.command(name = "скажи")
async def command_reply(ctx,*,text):
  await ctx.send(text)

@client.command()

async def дед (ctx):

  await ctx.reply(f"{ctx.author.mention} https://tenor.com/view/dead-inside-honk-ghoul-gif-21672383")





token = 'OTM1MTYzMTQ5MjE1MjE1Njg2.Ye6ojQ.eF1clUwbTnLig33-ZCNXEc_lprc' 


client.run(token)
