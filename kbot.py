# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
from tkn import TOKEN
from operate_cycle import *


def start(bot, update):
    text = "όνειρα γλυκά"
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)


def description(bot, update):
    text = "**Commands:** \n\n" \
           "/slew 26.12.2017\n" \
           "/unslew\n" \
           "/rewr 19.12.2017 3 12.12.2017\n" \
           "/cur\n" \
           "/nxt\n\n" \
           "**Shorthand:**\n\n" \
           "today\n" \
           "19.12\n" \
           "19"

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)


def slew(bot, update):
    # /slew 26.12.2017
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = query[1]
    except IndexError:
        query = ''
    reply = get_slew(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def unslew(bot, update):
    # /unslew
    query = update['message']['text']
    print('query:', query)
    reply = get_unslew()
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def rewr(bot, update):
    # /rewr 19.12.2017 3 12.12.2017
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = rewrite_file(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def cur(bot, update):
    # /cur
    query = update['message']['text']
    print('query:', query)
    reply = see_curr()
    print('reply:\n', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def nxt(bot, update):
    # /nxt
    query = update['message']['text']
    print('query:', query)
    reply = see_next()
    print('reply:\n', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', description)
    slew_handler = CommandHandler('slew', slew)
    unslew_handler = CommandHandler('unslew', unslew)
    rewr_handler = CommandHandler('rewr', rewr)
    cur_handler = CommandHandler('cur', cur)
    nxt_handler = CommandHandler('nxt', nxt)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(slew_handler)
    dispatcher.add_handler(unslew_handler)
    dispatcher.add_handler(rewr_handler)
    dispatcher.add_handler(cur_handler)
    dispatcher.add_handler(nxt_handler)

    updater.start_polling()
