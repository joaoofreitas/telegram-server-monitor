#!/usr/bin/python3

from requests import get
import  subprocess
import telebot

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

ip = get('https://api.ipify.org').text

def sensor():
    output = subprocess.run('sensors | awk "NR==3,NR==4"', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    output = output.stdout
    return output

def clientIPs():
    output = subprocess.run(r'netstat -tn 2>/dev/null | grep ":80\|22\|443" | awk "{print $5}" | cut -d: -f1 | sort | uniq -c | sort -nr | head', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    output = output.stdout
    return output

def keyboard():
    markup = telebot.types.ReplyKeyboardMarkup()
    
    showip_ =  telebot.types.KeyboardButton('What’s your IP address? 🌐')
    sensors_ =  telebot.types.KeyboardButton('How do you feel? 🌡️')
    listActive_ =  telebot.types.KeyboardButton('Show me your connections. 📝')

    markup.row(showip_)
    markup.row(sensors_, listActive_)

    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, Im Anton. How can I help you?", reply_markup=keyboard())


@bot.message_handler(commands=['showip'])
def showIP(message):
	bot.reply_to(message, "My IP Address is: " + ip)


@bot.message_handler(commands=['sensors'])
def sensors(message):
	bot.reply_to(message, "My sensors say that: \n\n" + sensor())


@bot.message_handler(commands=['listactive'])
def listIPs(message):
	bot.reply_to(message, "This is the list of current active IP Clients:  \n\n" + clientIPs())



@bot.message_handler(regexp="address?")
def handle_message_ip(message):
	bot.reply_to(message, "My IP Address is: " + ip)

@bot.message_handler(regexp="feel?")
def handle_message__temperature(message):
    bot.reply_to(message, "My sensors say that: \n\n" + sensor())

@bot.message_handler(regexp="connections.")
def handle_message_connections(message):
    bot.reply_to(message, "This is the list of current active IP Clients:  \n\n" + clientIPs())



@bot.message_handler(regexp="hello")
def handle_message(message):
	bot.reply_to(message, "What's up?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Sorry, didn't get that...")

bot.polling()

