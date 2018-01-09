# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
from tkn import TOKEN, AAS_ID, ADS_ID
from operate_cycle import *

NOAUTH = "This is a private bot"
ATTEMPT = "%d attempted %s"


def is_authorized(chat_id):
    return chat_id == AAS_ID or chat_id == ADS_ID


def start(bot, update):
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        text = NOAUTH
        print(ATTEMPT % (chat_id, '/start'))
    else:
        text = "όνειρα γλυκά"
    bot.send_message(chat_id=chat_id, text=text)


def description(bot, update):
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        text = NOAUTH
        print(ATTEMPT % (chat_id, '/help'))
    else:
        text = "Commands: \n\n" \
               "/slew 26.12.2017\n" \
               "/unslew\n" \
               "/rewr 19.12.2017 3 12.12.2017\n" \
               "/cur\n" \
               "/next\n" \
               "/cycle\n\n" \
               "Shorthand:\n\n" \
               "today\n" \
               "19.12\n" \
               "19"
    bot.send_message(chat_id=chat_id, text=text)


def slew(bot, update):
    # /slew 26.12.2017
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/slew'))
    else:
        query = update['message']['text']
        print('query:', query)
        query = query.split()
        try:
            query = query[1]
        except IndexError:
            query = ''
        reply = get_slew(query)
        print('reply:', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def unslew(bot, update):
    # /unslew
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/unslew'))
    else:
        query = update['message']['text']
        print('query:', query)
        reply = get_unslew()
        print('reply:', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def rewr(bot, update):
    # /rewr 19.12.2017 3 12.12.2017
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/rewr'))
    else:
        query = update['message']['text']
        print('query:', query)
        query = query.split()
        try:
            query = ' '.join(query[1:])
        except IndexError:
            query = ''
        reply = rewrite_file(query)
        print('reply:', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def cur(bot, update):
    # /cur
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/cur'))
    else:
        query = update['message']['text']
        print('query:', query)
        reply = see_curr()
        print('reply:\n', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def nxt(bot, update):
    # /next
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/next'))
    else:
        query = update['message']['text']
        print('query:', query)
        reply = see_next()
        print('reply:\n', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def cycle(bot, update):
    # /cycle 4
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/next'))
    else:
        query = update['message']['text']
        print('query:', query)
        query = query.split()
        try:
            query = query[1]
        except IndexError:
            query = ''
        reply = see_cycle(query)
        print('reply:', reply, '\n')
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
    nxt_handler = CommandHandler('next', nxt)
    cycle_handler = CommandHandler('cycle', cycle)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(slew_handler)
    dispatcher.add_handler(unslew_handler)
    dispatcher.add_handler(rewr_handler)
    dispatcher.add_handler(cur_handler)
    dispatcher.add_handler(nxt_handler)
    dispatcher.add_handler(cycle_handler)

    updater.start_polling()
