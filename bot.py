import telegram

TOKEN = "1093338802:AAEctvN5JSOc-XLM0yvOT-QG9-tZfk1F5AM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, Im Anton how can I help you?")