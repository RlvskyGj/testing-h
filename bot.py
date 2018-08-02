import telebot

bot =telebot.TeleBot('518126418:AAGQHyepa2vgecgoTbI3zON5kIRijjWbTYw')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
	bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
	bot.polling(none_stop=True)