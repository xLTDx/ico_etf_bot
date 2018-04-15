import telebot
from telebot import types

token = '521784656:AAHTwL9pzwUDns6E1e10UzUhVc6pKSZItlo'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Buy', 'Sell']])
    msg = bot.send_message(m.chat.id, 'Welcome to ICO - ETF bot!',
        reply_markup=keyboard)
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.text == 'Buy':
        bot.send_message(message.chat.id, 'To buy transfer your Ether to ...', parse_mode="Markdown")
    if message.text == 'Sell':
        bot.send_message(message.chat.id, 'To sell transfer your ETF Tokens to ...', parse_mode="Markdown")
		
bot.polling()

