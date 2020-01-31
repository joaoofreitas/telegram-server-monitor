#!/usr/bin/python3
import subprocess
import telebot


TOKEN = ""
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

bot.send_message("406247007", alert)