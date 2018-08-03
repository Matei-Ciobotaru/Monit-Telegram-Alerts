#!/usr/bin/python2.7

# -*- coding: utf-8 -*- #

# Author = Matei Ciobotaru

"""

      This script is used to send
      Telegram notifications when
      a Monit alarm is raised. 

"""

import os
from telegram.bot import Bot
from telegram.error import TelegramError
import logging as log

# Enable logging

log_file = '/var/log/monit.log'

# Lower case the log level to match the 'monit.log' format

log.addLevelName(log.INFO, 'info')
log.addLevelName(log.ERROR, 'error')

log.basicConfig(filename=log_file,
                format='[%(asctime)s] %(levelname)-9s: %(message)s', datefmt="%Z %b  %-d %H:%M:%S",level=log.INFO)

# MonitAlertBot details 
# Add your token & chatid here 

token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
chatid = 999999999

# Monit email alert message information fields

alert_fields = ['HOST', 'DATE', 'EVENT', 'SERVICE', 'DESCRIPTION', 'ACTION']

# Obtain Monit alert fields via environment variables
# This is how Monit works...

def get_alert(alert_fields):

	alert_msg = []
	for f in alert_fields:
		var_name = 'MONIT_' + f
		var_value = os.environ.get(var_name)
		# Only send fields with a value and edit field name
		if var_value is not None:
			line = "<b>" + f.title() + "</b>: " + var_value.upper()
			alert_msg.append(line)
	message = '\n'.join(alert_msg)
	
	return message

# Connect to Telegram bot

def send_alert(token, chatid):

	bot = Bot(token=token)
	ID = chatid
	# Send static message when Monit raises an alert
	bot.sendMessage(chat_id=ID, parse_mode='HTML', text='<strong>*** MONIT ALERT ***</strong>\n\n{0}'.format(message))

# Error Handling

try:
	message = get_alert(alert_fields)
	send_alert(token, chatid)
	log.info("Alert sent successfully via Telegram")
except TelegramError as tg_err:
	log.error("Unable to send alert, Telegram error: %s" % tg_err)
except Exception as err:
	log.error("Unable to send alert via Telegram: %s" % err)
