from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8557981769:AAEbSlXKLxLtAW8c4iMDtyOoxitjs-kDlVE"

async def pin_new_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message:
        try:
            await context.bot.pin_chat_message(
                chat_id=message.chat.id,
                message_id=message.message_id,
                disable_notification=True
            )
        except:
            pass  # agar pin qilolmasa xato bermaydi

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, pin_new_message))

app.run_polling()
