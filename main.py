# cspell: disable
import logging
import os
from pprint import pprint

import telebot
from telebot.types import (
    Message,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telebot.util import content_type_media

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN", "")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message: Message):
    reply_markup = InlineKeyboardMarkup()
    reply_markup.add(
        InlineKeyboardButton(
            "Web App",
            web_app=WebAppInfo(
                url="https://hamletsargsyan.github.io/telegrem-webapp-test/"
            ),
        )
    )

    bot.send_message(message.chat.id, "Hello World", reply_markup=reply_markup)


@bot.message_handler(content_types=content_type_media)
def log_message(message: Message):
    pprint(message.json, indent=4)


def main():
    telebot.logger.setLevel(logging.INFO)
    bot.infinity_polling()


if __name__ == "__main__":
    main()
