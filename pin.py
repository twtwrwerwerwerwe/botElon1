from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import logging

TOKEN = "8557981769:AAEbSlXKLxLtAW8c4iMDtyOoxitjs-kDlVE"

# PIN QILINADIGAN BOT USERNAME ( @siz yoziladi )
TARGET_BOT_USERNAME = "rishtonBogdodToshkentTaxi_bot"

logging.basicConfig(level=logging.INFO)

async def pin_only_target_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message or update.channel_post
    if not message:
        return

    # from_user bo‘lmasa — chiqib ketamiz
    if not message.from_user:
        return

    # ❗ FAQAT ANIQ BOT USERNAME
    if message.from_user.username != TARGET_BOT_USERNAME:
        return

    try:
        await context.bot.pin_chat_message(
            chat_id=message.chat.id,
            message_id=message.message_id,
            disable_notification=True
        )
        logging.info("📌 TARGET BOT XABARI PIN QILINDI")
    except Exception as e:
        logging.error(f"❌ PIN XATO: {e}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, pin_only_target_bot))

print("✅ Bot ishga tushdi")

app.run_polling(
    allowed_updates=["message", "channel_post"]
)
