import datetime
import bot

if __name__ == '__main__':
    # Запускаем бота
    print("Bot is started at", (datetime.datetime.now()))
    bot.start_bot()
    print("Bot is finished without errors at", datetime.datetime.now())