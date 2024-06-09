from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"Hello, {user.first_name}!")

# Обработчик текстовых сообщений
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Функция для создания и запуска бота
def main():
    # Инициализация бота
    updater = Updater("7484546517:AAFqufJ4vGvaQcNbTBuE-d6GHuRo8rmqH_I", use_context=True)
    dp = updater.dispatcher

    # Добавление обработчиков команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()