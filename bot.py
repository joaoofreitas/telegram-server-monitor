from requests import get
import  subprocess
import telebot


TOKEN = "1093338802:AAEctvN5JSOc-XLM0yvOT-QG9-tZfk1F5AM"
bot = telebot.TeleBot(TOKEN)

ip = get('https://api.ipify.org').text


def sensor():
    output = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return output

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, Im Anton. How can I help you?")


@bot.message_handler(commands=['showip', 'help'])
def showIP(message):
	bot.reply_to(message, "My IP Address is: " + ip)


@bot.message_handler(commands=['sensors', 'help'])
def sensors(message):
	bot.reply_to(message, "My sensors say that: " + sensor())

bot.polling()


'''

showip - Show my IP
sensors - How do I feel right now
'''
