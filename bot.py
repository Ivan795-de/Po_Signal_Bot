from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я бот по сигналам для Pocket Option 📊")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    directions = ['CALL (вгору) 📈', 'PUT (вниз) 📉']
    pairs = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'AUD/CAD']
    signal = f"{random.choice(pairs)} → {random.choice(directions)}"
    await update.message.reply_text(f"Сигнал: {signal}")

app = ApplicationBuilder().token("ВСТАВ_ТУТ_СВІЙ_ТОКЕН").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Po_Signal_Bot запущений ✅")
app.run_polling()
