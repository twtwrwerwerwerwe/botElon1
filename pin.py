from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import logging

TOKEN = "8557981769:AAEbSlXKLxLtAW8c4iMDtyOoxitjs-kDlVE"

logging.basicConfig(level=logging.INFO)

async def pin_bot_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message or update.channel_post
    if not message:
        return

    # ❗ FAQAT BOT YOZGAN XABARLAR
    if not message.from_user or not message.from_user.is_bot:
        return

    try:
        await context.bot.pin_chat_message(
            chat_id=message.chat.id,
            message_id=message.message_id,
            disable_notification=True
        )
        logging.info("📌 BOT XABARI PIN QILINDI")
    except Exception as e:
        logging.error(f"❌ PIN XATO: {e}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, pin_bot_messages))

print("✅ Bot ishga tushdi")

app.run_polling(
    allowed_updates=["message", "channel_post"]
)
