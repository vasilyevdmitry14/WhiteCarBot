from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True) # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling() # Командуем боту начать ходить в Telegram за сообщениями
    mybot.idle() # Запускаем бота, он будет работать, пока мы его не остановим принудительно


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


if __name__ == "__main__":
    main()
