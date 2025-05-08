"""
Telegram bot with mini-app integration.
"""

import logging
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import BOT_TOKEN, WEBAPP_URL

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Handler for /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    # Create a keyboard with a button that opens the mini-app
    webapp_button = InlineKeyboardButton(
        text="Заполнить форму",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = InlineKeyboardMarkup().add(webapp_button)

    await message.answer(
        "Привет! Я бот для сбора данных. Нажмите на кнопку ниже, чтобы открыть форму:",
        reply_markup=keyboard
    )

# Handler for web app data
@dp.message_handler(content_types=types.ContentTypes.WEB_APP_DATA)
async def web_app_handler(message: types.Message):
    """
    This handler will be called when user sends data from the web app
    """
    # Get data from web app
    data = json.loads(message.web_app_data.data)

    # Log received data
    logging.info(f"Received data: {data}")

    # Send confirmation message
    await message.answer("Спасибо, ваша заявка принята!")

    # You can also send a detailed confirmation with the submitted data
    details = "\n".join([f"{key}: {value}" for key, value in data.items()])
    await message.answer(f"Полученные данные:\n{details}")

# Main entry point
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)