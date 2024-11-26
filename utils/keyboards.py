from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def reply_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("Добавить задачу")],
            [KeyboardButton("Показать задачи")],
            [KeyboardButton("Очистить список")]
        ],
        resize_keyboard=True
    )

def confirm_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Подтвердить", callback_data="confirm")],
            [InlineKeyboardButton(text="Отменить", callback_data="cancel")]
        ]
    )
