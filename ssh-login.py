#!/usr/bin/python3
from json import loads as jsonloads
import subprocess
import telebot

def get_folder():
    folder = subprocess.run(r'pwd', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    folder = folder.stdout
    return folder[:0]

try:
    with open(get_folder() + 'config.json', 'r') as configFile:
        config = configFile.read()
    file = jsonloads(config)

    TOKEN = file["TOKEN"]
    CHAT_ID = file["CHAT_ID"]

except NameError:
    print("ERROR IMPORTING the config.json file, please check your absolute path or folder permissions")


bot = telebot.TeleBot(TOKEN)

#put this script running on /etc/bash.bashrc

def get_ip():
    ip_address = subprocess.run(r'echo $SSH_CONNECTION | cut -d " " -f 1', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    ip_address = ip_address.stdout
    return ip_address

def get_user():
    username = subprocess.run(r'echo $USER', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    username = username.stdout
    return username

alert = "User " + get_user() + "login made on ip: "  + get_ip()

bot.send_message(CHAT_ID, alert)