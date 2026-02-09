import telebot
from bot.handlers import register_handlers
from bot.config import BOT_TOKEN

def main():
    bot = telebot.TeleBot(BOT_TOKEN)
    register_handlers(bot)
    print('LogiControl Bot started')
    bot.infinity_polling()

if __name__ == '__main__':
    main()
    
   