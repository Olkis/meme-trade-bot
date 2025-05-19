import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, JobQueue
from dotenv import load_dotenv
from utils.data_sources import get_token_volume, get_liquidity
from utils.indicators import check_ema_cross, check_candle_pattern
from utils.risk_filters import check_contract, check_liquidity, load_callers_whitelist
from utils.virality import check_virality

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

<<<<< HEAD
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
=======
# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
>>>>>>> c22c2e6685aa835f90199bb3c5544b5ee7f70395

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Команда /start получена")
    await update.message.reply_text("👋 Привет! Я трейдинг-бот. Ожидай сигналов...")

<<<<<<< HEAD
async def check_flip_signal(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.data.get('chat_id')
    if not chat_id:
        logger.error("chat_id не найден в контексте для FLIP")
        return
    try:
        token_address = "SAMPLE_TOKEN_ADDRESS"
        volume = await get_token_volume(token_address)
        liquidity = await get_liquidity(token_address)
        ema_cross = await check_ema_cross(token_address, "1m")
        candle_pattern = await check_candle_pattern(token_address, "1m")
        contract_ok = await check_contract(token_address)
        liquidity_ok = await check_liquidity(token_address, 2000)
        virality_ok = await check_virality("CATMOON", token_address)

        if (volume > 100000 and ema_cross and candle_pattern and contract_ok and
            liquidity_ok and virality_ok):
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"🚀 Сигнал FLIP\nМонета: $CATMOON\nОбъём: ${volume}\nЛиквидность: ${liquidity}\nПроверка пройдена ✅"
            )
            logger.info("Сигнал FLIP отправлен")
        else:
            logger.info("Условия для FLIP не выполнены")
    except Exception as e:
        logger.error(f"Ошибка в check_flip_signal: {e}")

async def check_level_signal(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.data.get('chat_id')
    if not chat_id:
        logger.error("chat_id не найден в контексте для LEVEL")
        return
    try:
        token_address = "SAMPLE_TOKEN_ADDRESS"
        volume = await get_token_volume(token_address)
        liquidity = await get_liquidity(token_address)
        ema_cross = await check_ema_cross(token_address, "5m")
        candle_pattern = await check_candle_pattern(token_address, "5m")
        contract_ok = await check_contract(token_address)
        liquidity_ok = await check_liquidity(token_address, 5000)
        virality_ok = await check_virality("LEVEL_TOKEN", token_address)

        if (volume > 20000 and ema_cross and candle_pattern and contract_ok and
            liquidity_ok and virality_ok):
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"🚀 Сигнал LEVEL\nМонета: $LEVEL_TOKEN\nОбъём: ${volume}\nЛиквидность: ${liquidity}\nПроверка пройдена ✅"
            )
            logger.info("Сигнал LEVEL отправлен")
        else:
            logger.info("Условия для LEVEL не выполнены")
    except Exception as e:
        logger.error(f"Ошибка в check_level_signal: {e}")

async def set_monitoring(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if not chat_id:
        logger.error("Не удалось определить chat_id")
        await update.message.reply_text("Ошибка: не удалось определить chat_id")
        return
    try:
        # Убедимся, что JobQueue инициализирован
        if context.job_queue is None:
            logger.error("JobQueue не инициализирован")
            await update.message.reply_text("Ошибка: JobQueue не работает")
            return
        context.job_queue.run_repeating(check_flip_signal, interval=60, first=0, data={'chat_id': chat_id})
        context.job_queue.run_repeating(check_level_signal, interval=300, first=0, data={'chat_id': chat_id})
        await update.message.reply_text("Мониторинг FLIP и LEVEL запущен! Проверка каждые 60s и 300s.")
        logger.info(f"Мониторинг запущен для chat_id: {chat_id}")
    except Exception as e:
        logger.error(f"Ошибка при запуске мониторинга: {e}")
        await update.message.reply_text(f"Ошибка при запуске мониторинга: {e}")
=======
# Обработчик команды /test
async def test_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 [TEST] Новый сигнал: FLIP\nМонета: $CATMOON\nОбъём: $115K\nПроверка пройдена ✅"
    )
>>>>>>> c22c2e6685aa835f90199bb3c5544b5ee7f70395

# Основная функция
def main():
<<<<<<< HEAD
    if not TOKEN:
        print("Ошибка: TELEGRAM_BOT_TOKEN не найден в .env")
        return

    # Явная инициализация JobQueue
    app = ApplicationBuilder().token(TOKEN).job_queue(JobQueue()).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("monitor", set_monitoring))

    print("Бот запускается...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
=======
    # Создаём приложение
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_signal))

    # Запускаем бота
    app.run_polling()
>>>>>>> c22c2e6685aa835f90199bb3c5544b5ee7f70395

if __name__ == "__main__":
    main()