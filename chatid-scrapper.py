#!/usr/bin/python3
import telebot
import subprocess
from requests import get
from json import loads as jsonloads

def get_folder():
    folder = subprocess.run('pwd', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    folder = folder.stdout
    return folder[:0]

class json_Update:
    def CHAT_ID_fetcher(self):
        try:    
            with open(get_folder() + 'getUpdates.json', 'r') as updatesFile:
                updates = updatesFile.read()
            updateFile = jsonloads(updates)
            output = updateFile["result"][0]["message"]["from"]["id"]
            return str(output)

        except:
            print("ERROR IMPORTING the getUpdates.json file for reading, please check your absolute path or folder permissions")


    def writeUpdates(self,FETCH):
        try:    
            with open(get_folder() + 'getUpdates.json', 'w+') as updatesFile:
                updatesFile.write(FETCH)

        except:
            print("ERROR IMPORTING the getUpdates.json file, for writing, please check your absolute path or folder permissions")


try:
    with open(get_folder() + 'config.json', 'r') as configFile:
        config = configFile.read()
    file = jsonloads(config)

    TOKEN = file["TOKEN"]
    CHAT_ID = file["CHAT_ID"]

except:
    print("ERROR IMPORTING the config.json file, please check your absolute path or folder permissions")

FETCH = get('https://api.telegram.org/bot' + TOKEN +'/getUpdates').text

getUpdates = json_Update()
getUpdates.writeUpdates(FETCH)
CHAT_ID = getUpdates.CHAT_ID_fetcher()