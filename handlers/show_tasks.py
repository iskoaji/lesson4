from aiogram import types, F, Router
from database import get_tasks
from utils.keyboards import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(F.text == "Показать задачи")
async def show_tasks(message: types.Message):
    user_id = message.from_user.id
    tasks = get_tasks(user_id)

    if not tasks:
        await message.answer("У вас пока нет задач.")
        return

    buttons = [
        InlineKeyboardButton(text=f"{task[1][:30]}...", callback_data=f"task_{task[0]}")
        for task in tasks
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])

    await message.answer("Ваши задачи:", reply_markup=keyboard)
