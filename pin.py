from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import logging

TOKEN = "8557981769:AAEbSlXKLxLtAW8c4iMDtyOoxitjs-kDlVE"
TARGET_BOT_USERNAME = "rishtonBogdodToshkentTaxi_bot"

logging.basicConfig(level=logging.INFO)

async def pin_target_bot_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message or update.channel_post
    if not message:
        return

    # 🔹 from_user mavjud va username mos bo‘lsa
    if message.from_user and message.from_user.username == TARGET_BOT_USERNAME:
        pass
    # 🔹 sender_chat mavjud va username mos bo‘lsa (anonymous botlar uchun)
    elif message.sender_chat and message.sender_chat.username == TARGET_BOT_USERNAME:
        pass
    else:
        return  # boshqa odam yoki bot bo‘lsa, chiqib ketamiz

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
app.add_handler(MessageHandler(filters.ALL, pin_target_bot_message))

print("✅ Bot ishga tushdi")

app.run_polling(drop_pending_updates=True, allowed_updates=["message", "channel_post"])
