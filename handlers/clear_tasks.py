from aiogram import types, F, Router
from database import clear_tasks
from utils.keyboards import confirm_keyboard

router = Router()

@router.message(F.text == "Очистить список")
async def clear_tasks_prompt(message: types.Message):
    await message.answer("Вы уверены, что хотите удалить все задачи?", reply_markup=confirm_keyboard())

@router.callback_query(lambda call: call.data == "confirm")
async def confirm_clear(call: types.CallbackQuery):
    user_id = call.from_user.id
    clear_tasks(user_id)
    await call.message.answer("Все задачи удалены.")
    await call.answer()

@router.callback_query(lambda call: call.data == "cancel")
async def cancel_clear(call: types.CallbackQuery):
    await call.message.answer("Удаление отменено.")
    await call.answer()
