from requests import get
import  subprocess
import telebot

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

ip = get('https://api.ipify.org').text

def sensor(command):
    output = subprocess.run(['vcgencmd', command], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return output

def clientIPs():
    output = subprocess.run(['netstat', '-t', '2>/dev/null', '|', 'awk', "'{print $5}'", '|', 'cut', '-d:', '-f1', '|', 'sort', '|',  'uniq', '-c', '|', 'sort'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return output


markup = telebot.types.ReplyKeyboardMarkup()

showip_ =  telebot.types.KeyboardButton('/showip 🌐')
sensors_ =  telebot.types.KeyboardButton('/sensors 🌡️')
listActive_ =  telebot.types.KeyboardButton('/listactive 📝')
markup.row(showip_)
markup.row(sensors_, listActive_)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, Im Anton. How can I help you?", reply_markup=markup)


@bot.message_handler(commands=['showip', 'help'])
def showIP(message):
	bot.reply_to(message, "My IP Address is: " + ip)


@bot.message_handler(commands=['sensors', 'help'])
def sensors(message):
	bot.reply_to(message, "My sensors say that: " + subprocess.run(['sensors'], stdout=subprocess.PIPE).stdout.decode('utf-8')) #sensor('measure_temp') + sensor('measure_volts'))


@bot.message_handler(commands=['listactive', 'help'])
def listIPs(message):
	bot.reply_to(message, "This is the list of current active IP Clients:  \n" + clientIPs())


@bot.message_handler(regexp="hello")
def handle_message(message):
	bot.reply_to(message, "What's up?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Sorry, didn't get that...")
bot.polling()


'''
showip - Show my IP
sensors - How do I feel right now
listactive - //netstat -t 2>/dev/null | awk '{print $5}' | cut -d: -f1 | sort |  uniq -c | sort
'''
