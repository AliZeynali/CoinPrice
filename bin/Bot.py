import requests
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from Crawler import getCoinPrices


markupStart = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Get Data")]])
coin_address = "https://coinmarketcap.com/all/views/all/"



def on_chat_message(message):
    global current
    content_type, chat_type, chat_id = telepot.glance(message)
    global markupStart, coin_address
    # print(message)
    if content_type == 'text':
        text = message['text']
        text = text.replace("/", "")
        markup = markupStart
        if text == 'start':
            bot.sendMessage(chat_id, "سلام!", reply_markup=markup)

        if text == 'Get Data':
            bot.sendMessage(chat_id, "Collecting Data, be patient...", reply_markup=None)
            text_chat = getCoinPrices(coin_address)
            bot.sendMessage(chat_id, text_chat, reply_markup=markup)




if __name__ == "__main__":
    token = "541493008:AAFQwyHp-1EiIESg-P3aH2jBFZjI6vyqt-4"
    bot = telepot.Bot(token)

    bot.message_loop({'chat': on_chat_message})

    while True:
        time.sleep(10)
