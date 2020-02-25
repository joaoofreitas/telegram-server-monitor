# server-telegram-monitor
Small project, that I use to monitor my small RaspberryPi server, without SSH.

#### Instalation
##### Requirements
These are the following requirements:
1. python-pip3
2. python3
3. pyTelegramBotAPI

##### Scripting
I will create a bash script that will take care of all that for you.
Stay tuned.

##### Configuring and running the bot
For now, you can just run the bot.py on the startup and it will be running!
Run the _ssh-login.py_ so it sends you a message on a user SSH login, so you can control who is acesssing
your server.

*(In case you are new at this)*
For running the bot use: 

> git clone https://github.com/joaoofreitas/telegram-server-monitor.git

> cd telegram-server-monitor

> python3 bot.py

> python3 ssh-login


This are the basic commands for running the bot.








Features:
1. Public IP Address Fetcher
2. Temperature Fetcher
3. Connected IP's list
4. Warning message on ssh login.

To do:
1. Add an installation
2. Performance Upgrade (even though is really fast).
