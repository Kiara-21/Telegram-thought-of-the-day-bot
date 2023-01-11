#May Omnissiah forgive me my sins and bless this code. Amen.

import random
import time
import telegram.ext

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from time import sleep

Token = "5900748455:AAHsYRloVvw0tktlGm9uCFry4Jiafbnr3R4"

updater = telegram.ext.Updater("5900748455:AAHsYRloVvw0tktlGm9uCFry4Jiafbnr3R4", use_context=True)
dispatcher = updater.dispatcher

messages_text = ['"Одна тільки сила волі може змінити Всесвіт"',
                 '"Перемога або смерть!"',
                 '"Віра - мій щит. Лють - мій меч."',
                 '"Рандомна пафосна цитата"']

def start(update, context):
    update.message.reply_text("Ця благословенна програма публікує цитати. Введіть /send_msg для початку роботи.")

def send_msg(update, context):
    msg_handler = True
    while msg_handler == True:
        txmsg = random.choice(messages_text)
        context.bot.sendMessage(chat_id='-852220279', text=txmsg)
        time.sleep(21600)

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('send_msg', send_msg))


updater.start_polling()
updater.idle()