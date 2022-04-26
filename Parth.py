from pyrogram import Client,filters

bot = Client(
    "First Bot",
    api_id=16634851,
    api_hash="2a10c50d07c5a2a90b811eeebb45b79d",
    bot_token="5125346839:AAEg7k03YgVvDvaZEpF88Q86YL197s0JhnY"
)
@bot.on_message(filters.command('start'))
def command1(bot, message):
    message.reply_text('WTF do u want from me? LEAVE ME ALONE!!')
@bot.on_message(filters.command('help'))
def command1(bot, message):
    message.reply_text('Go Help urself :|')
    #echobot
@bot.on_message(filters.text & filters.private )
def echobot(Client, message):
    message.reply_text(message.text)
    
@bot.on_message(filters.command('pic'))
def command1(bot, message):
    bot.send_photo(message.chat.id,'https://www.google.com/url?sa=i&url=https%3A%2F%2Fnewsbeezer.com%2Fperueng%2Fdemon-slayer-who-is-tanjiro-kamado-the-protagonist-of-kimetsu-no-yaiba-guardian-of-the-night-anime-series-fame%2F&psig=AOvVaw3SvC7NzOyfcdKUK8MLbtFI&ust=1643722190300000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMiOkcWM3PUCFQAAAAAdAAAAABAJ')


bot.run()
