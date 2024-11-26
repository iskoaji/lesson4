from aiogram import types, Router, F
from aiogram import FSMContext
from aiogram import State, StatesGroup
from database import add_task

router = Router()

class TaskState(StatesGroup):
    waiting_for_task_text = State()

@router.message(F.text == "Добавить задачу")
async def add_task_prompt(message: types.Message, state: FSMContext):
    await message.answer("Введите текст задачи:")
    await state.set_state(TaskState.waiting_for_task_text)

@router.message(TaskState.waiting_for_task_text)
async def save_task(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    task_text = message.text
    add_task(user_id, task_text)
    await message.answer("Задача добавлена!")
    await state.clear()
