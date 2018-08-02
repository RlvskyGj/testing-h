import telebot

bot = telebot.TeleBot('518126418:AAGQHyepa2vgecgoTbI3zON5kIRijjWbTYw')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

if __name__ == '__main__':
	bot.polling()