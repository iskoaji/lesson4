from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from database import init_db
from handlers.start import router as start_router
from handlers.add_task import router as add_task_router
from handlers.show_tasks import router as show_tasks_router
from handlers.clear_tasks import router as clear_tasks_router
from config import TOKEN

def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(add_task_router)
    dp.include_router(show_tasks_router)
    dp.include_router(clear_tasks_router)

    init_db()

    bot_commands = [
        BotCommand(command="/start", description="Запустить бота")
    ]
    bot.set_my_commands(bot_commands)

    dp.run_polling(bot)

if __name__ == "__main__":
    main()










"callback_query"="url"