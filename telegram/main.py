from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from bot_utils import print_meta

def main():
    try:
        updater = Updater("token", use_context=True)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(MessageHandler(Filters.all, print_meta))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()