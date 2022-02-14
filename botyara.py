import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def aboba(message):
	bot.send_message(message.chat.id, message.text)

 # pusk
bot.polling(none_stop=True)