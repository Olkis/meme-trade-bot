import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Настраиваем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Я трейдинг-бот. Ожидай сигналов...")

# Обработчик команды /test
async def test_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 [TEST] Новый сигнал: FLIP\nМонета: $CATMOON\nОбъём: $115K\nПроверка пройдена ✅"
    )

# Основная функция
def main():
    # Проверяем, что токен существует
    if not TOKEN:
        print("Ошибка: TELEGRAM_BOT_TOKEN не найден в .env")
        return

    # Создаём приложение
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_signal))

    # Запускаем бота
    print("Бот запускается...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()