# Sending Monit alerts via Telegram

 A simple python script I wrote so I may send [Monit](https://mmonit.com/monit/) alerts via Telegram.

## Python Libraries

 You will require the [python-telegram-bot](https://python-telegram-bot.org/) library to use Telegram.

## Telegram Bot

 You will need to create a Telegram bot and edit the python script to add your personal BOT_TOKEN and CHAT_ID.

 Details on how to create a bot [here](https://core.telegram.org/bots#creating-a-new-bot).

## Description

**monit_alert.py**<br>

 By default, Monit uses a set of environment variables to store details of the alert which it sends via email.
 This script grabs the output of the aformentioned variables, formats them for readability and sends them via Telegram.
 It also writes its output in Monit's default log ('/var/log/monit.log') using the same format for debugging purposes.

**monitrc**<br>

 This is an extract from my Monit instance's configuration file, which shows how to set Telegram alerts for a service.

**monit.log**<br>

 An extract of the Monit log containing a Telegram alert script entry.

## Example Telegram alert

<img src="https://i.imgur.com/JOztEqF.jp" height="400" width="400">
