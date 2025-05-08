"""
Telegram bot with mini-app integration using pyTelegramBotAPI (TeleBot).
"""

import logging
import json
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import BOT_TOKEN, WEBAPP_URL

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    This handler will be called when user sends `/start` command
    """
    # Create a keyboard with a button that opens the mini-app
    markup = InlineKeyboardMarkup()
    webapp_button = InlineKeyboardButton(
        text="Заполнить форму",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    markup.add(webapp_button)

    bot.send_message(
        message.chat.id,
        "Привет! Я бот для сбора данных. Нажмите на кнопку ниже, чтобы открыть форму:",
        reply_markup=markup
    )

# Handler for web app data
@bot.message_handler(content_types=['web_app_data'])
def web_app_handler(message):
    """
    This handler will be called when user sends data from the web app
    """
    # Get data from web app
    data = json.loads(message.web_app_data.data)

    # Log received data
    logging.info(f"Received data: {data}")

    # Send confirmation message
    bot.send_message(message.chat.id, "Спасибо, ваша заявка принята!")

    # You can also send a detailed confirmation with the submitted data
    details = "\n".join([f"{key}: {value}" for key, value in data.items()])
    bot.send_message(message.chat.id, f"Полученные данные:\n{details}")

# Main entry point
if __name__ == '__main__':
    logging.info("Starting bot...")
    bot.infinity_polling()