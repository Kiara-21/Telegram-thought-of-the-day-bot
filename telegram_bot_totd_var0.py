#May Omnissiah forgive me my sins and bless this code. Amen.

import random
import time
import telegram.ext

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from time import sleep

Token = "INSERT YOUR TOKEN HERE"

updater = telegram.ext.Updater("INSERT YOUR TOKEN HERE", use_context=True)
dispatcher = updater.dispatcher

messages_text = ['"Put random epic wh40k sentences in this array"']

def start(update, context):
    update.message.reply_text("Random epic throught 4 times per day. Type /send_msg to start.")

def send_msg(update, context):
    msg_handler = True
    while msg_handler == True:
        txmsg = random.choice(messages_text)
        context.bot.sendMessage(chat_id='INSERT YOUR CHAT ID HERE', text=txmsg)
        time.sleep(21600)

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('send_msg', send_msg))


updater.start_polling()
updater.idle()
