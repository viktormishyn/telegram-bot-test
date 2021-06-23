import os
from dotenv import load_dotenv
from telegram.ext import *  # TODO define which dependencies really needed
import Responses as R

load_dotenv()
# load env variables
BOT_API_KEY = os.environ.get('BOT_API_KEY')

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Say something!)')


def help_command(update, context):
    update.message.reply_text(
        'If you need help, you should ask for it on Google=))')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(BOT_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()