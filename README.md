# Telegram Server Monitor 💻
Small project that I use to monitor my small RaspberryPi server, without SSH. On any device...

### How was it build? 🐍
I created this project using only Python3 and _[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)_ with embedded _bash_ scripting to generate the messages.

### Installation
##### Requirements 📲
These are the following requirements:
1. python-pip3
2. python3
3. pyTelegramBotAPI

##### Installation 🤖
I will create a bash script that will take care of all that for you. But for now you can follow the instructions below if you really want to try this up.

Stay tuned.

##### Configuring and running the bot 🤖

For now, you can just run the bot.py on the startup and it will be running!
Run the _ssh-login.py_ so it sends you a message on a user SSH login, so you can control who is accessing
your server.

*(In case you are new at this)*
For installing the bot use: 

`git clone https://github.com/joaoofreitas/telegram-server-monitor.git`

`cd telegram-server-monitor`

Before you run the bot. You should create a bot with @BotFather and config your _config.json_ file and put your API Token and CHATID provided.
(You can see more details at https://core.telegram.org/bots)

After this you can run the bot using the following commands:

`python3 bot.py`

`python3 ssh-login.py`

To install all this, you should run the file ssh-login.py in your bash.bashrc file located in /etc/bash.bashrc.
With this, the bot will send you a message on bash login each time a user logs in.

After you can create a systemctl service or what works best for you to run the bot on startup.
Any questions you can message me on Twitter or open a issue here no git, I will be glad to help.

### Usage 📟

After running the bot. You can access your telegram and use _/start_ on your bot. And start messaging him!
Just has easy has it gets 😎

### Features and Future Updates 🚀
Features:
1. Public IP Address Fetcher
2. Temperature Fetcher
3. Connected IP's list
4. Warning message on ssh login.

Future Updates:
1. Add an installation
2. Performance Upgrade.

### Example
| ![1](https://user-images.githubusercontent.com/31630346/75636871-6b75aa80-5c1a-11ea-80bc-5d5dd1f164d9.jpeg) | ![2](https://user-images.githubusercontent.com/31630346/75636874-76c8d600-5c1a-11ea-8a2c-8815ff51a27c.jpeg) | ![3](https://user-images.githubusercontent.com/31630346/75636879-7c262080-5c1a-11ea-809c-47a3f5e56381.jpeg) |
|:---:|:---:|:---:|


Thank you guys for the support, as I said, feel free to chat with me about this or any other project. 
