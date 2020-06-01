#!/usr/bin/python3
# -*- coding: utf-8 -*- #

"""

 This script is used to send Telegram notifications
 when a Monit alert is raised.

 Author = Matei Ciobotaru

"""


import os
import logging
from telegram.bot import Bot
from telegram.error import NetworkError, TelegramError


# Enable logging
LOG_FILE = '/var/log/monit.log'

# Lower case the log level and add spaces to match the 'monit.log' format
logging.addLevelName(logging.INFO, 'info')
logging.addLevelName(logging.ERROR, 'error')

logging.basicConfig(filename=LOG_FILE,
                    format='[%(asctime)s] %(levelname)-9s: %(message)s',
                    datefmt="%Z %b  %-d %H:%M:%S", level=logging.INFO)

# Monit alert bot info
BOT_TOKEN = 'YOUR_SECRET_BOT_TOKEN'
CHAT_ID = 'YOUR_SECRET_CHAT_ID'

# Monit Telegram message information fields
ALERT_FIELDS = ['HOST', 'DATE', 'EVENT', 'SERVICE', 'DESCRIPTION']


def alert_message(alert_fields):
    """
    Obtain Monit alert details via environment variables
    """

    header = '🔔 <b>MONIT ALERT</b> 🔔\n\n'
    message_lines = []

    for field in alert_fields:

        variable = 'MONIT_' + field
        field_value = os.environ.get(variable, 'N/A')

        field_name = '<b>{0}: </b>'.format(field.title())
        line = field_name + field_value.upper()

        message_lines.append(line)

    message = header + '\n'.join(message_lines)

    return message


def send_alert(token, chatid, message):
    """
    Send Telegram alert message
    """

    try:
        bot = Bot(token=token)
        bot.send_message(chat_id=chatid, parse_mode='HTML', text='{0}'.format(message))
        logging.info("Alert successfully sent via Telegram.")
    except (NetworkError, TelegramError) as tg_err:
        logging.error("Unable to send alert, Telegram exception: %s", tg_err)


def main():
    """
    Script excecution
    """

    message = alert_message(ALERT_FIELDS)
    send_alert(BOT_TOKEN, CHAT_ID, message)


if __name__ == '__main__':
    main()
