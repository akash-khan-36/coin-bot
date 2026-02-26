import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
import threading
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Open Dashboard",
                web_app=WebAppInfo(url="https://example.com")
            )]
        ]
    )
    await message.answer("Welcome to Coin Sell Bot", reply_markup=kb)

async def run_bot():
    await dp.start_polling(bot)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Running"

def run_web():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    asyncio.run(run_bot())
