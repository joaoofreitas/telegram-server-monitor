#!/usr/bin/python3
from json import loads as jsonloads
from requests import get
import  subprocess
import telebot

def get_folder():
    folder = subprocess.run('pwd', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    folder = folder.stdout
    return folder[:0]

try:
    with open(get_folder() + 'config.json', 'r') as configFile:
        config = configFile.read()
    file = jsonloads(config)
    
    TOKEN = file["TOKEN"]
    CHAT_ID = file["CHAT_ID"]
    WHITELIST = file["WHITELIST"]
    

except:
    print("ERROR IMPORTING the config.json file, please check your absolute path or folder permissions")

bot = telebot.TeleBot(TOKEN)
ip = get('https://api.ipify.org').text

def sensor():
    temp = subprocess.run(r'cat /sys/class/thermal/thermal_zone0/temp', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    temp = temp.stdout
    sensorVal = int(temp) / 1000
    
    output = str(sensorVal) + 'ºC'
    return output

def clientIPs():
    command = r"netstat -anp --tcp | awk '{print $5}' | awk 'NR==5,NR==5000'"
    output = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
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
    username = message.chat.username
    if(username not in WHITELIST):
       bot.reply_to(message, "I don't know you... Bye")
    else:
        bot.reply_to(message, "Hello, Im Anton. How can I help you?", reply_markup=keyboard())
    

@bot.message_handler(commands=['showip'])
def showIP(message):
	bot.reply_to(message, "My IP Address is: " + ip)


@bot.message_handler(commands=['sensors'])
def sensors(message):
	bot.reply_to(message, "My sensors say that my temperature is: " + sensor())


@bot.message_handler(commands=['listactive'])
def listIPs(message):
	bot.reply_to(message, "This is the list of current active IP Clients:  \n\n" + clientIPs())



@bot.message_handler(regexp="address?")
def handle_message_ip(message):
	bot.reply_to(message, "My IP Address is: " + ip)

@bot.message_handler(regexp="feel?")
def handle_message__temperature(message):
    bot.reply_to(message, "My sensors say that my temperature is: " + sensor())

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


