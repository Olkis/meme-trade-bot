import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Я трейдинг-бот. Ожидай сигналов...")

async def test_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 [TEST] Новый сигнал: FLIP\nМонета: $CATMOON\nОбъём: $115K\nПроверка пройдена ✅")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_signal))
    app.run_polling()

if __name__ == "__main__":
    main()
