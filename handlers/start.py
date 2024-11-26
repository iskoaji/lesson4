from aiogram import types, Router
from utils.keyboards import reply_keyboard

router = Router()

@router.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я помогу управлять вашими задачами. Выберите действие:",
        reply_markup=reply_keyboard()
    )
