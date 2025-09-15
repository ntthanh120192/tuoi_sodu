from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import logging

TOKEN = "606269662:AAETmBf86V6ojtoFsqL9uACmSER1yW10g9M"
SOURCE_CHAT = -1002934879278
TARGET_CHAT = -4676555674
MAX_LEN = 10

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

def on_message(update: Update, context: CallbackContext):
    msg = update.effective_message
    if not msg:
        return
    chat_id = update.effective_chat.id
    text = msg.text or ""
    if chat_id == SOURCE_CHAT:
        if text.startswith("VND ") and len(text) <= MAX_LEN:
            bot.forward_message(chat_id=TARGET_CHAT, from_chat_id=SOURCE_CHAT, message_id=msg.message_id)
            logging.info("Forwarded: %s", text)

if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, on_message))
    updater.start_polling()
    logging.info("Bot started")
    updater.idle()
