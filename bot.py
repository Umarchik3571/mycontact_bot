import logging

from aiogram import Bot, Dispatcher, executor, types
from lang_context import *
from bot_keyboard import *

BOT_TOKEN="6368924931:AAE5qnY4Y2Ssz3fV3xDTv2N9TWwLKELTUf8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    btn = await choose_lang_btn()
    await message.answer("Til tanlang:", reply_markup=btn)

@dp.callback_query_handler(text_contains='lang')
async def choose_lang_callback(call: types.CallbackQuery):
    # zz = await start_menu_btn()
    lang = call.data.split(":")[1]
    await call.message.delete()
    btn = await start_menu_btn(lang)
    await call.message.answer(context[lang]["start_text"],reply_markup=btn)

@dp.message_handler(text = "have I Premium?")
async def idret(message: types.Message):
    await message.reply(f"Your premium: {message.from_user.is_premium}")

@dp.message_handler(text = "My ID")
async def idret(message: types.Message):
    await message.reply(f"Your ID: {message.from_user.id}")

@dp.message_handler(text = "My username")
async def idret(message: types.Message):
    await message.reply(f"Your username: {message.from_user.username}")


@dp.message_handler(text = "У меня Premium?")
async def idret(message: types.Message):
    await message.reply(f"Ваш premium: {message.from_user.is_premium}")

@dp.message_handler(text = "Мой ID")
async def idret(message: types.Message):
    await message.reply(f"Ваш ID: {message.from_user.id}")

@dp.message_handler(text = "Мой username")
async def idret(message: types.Message):
    await message.reply(f"Ваш username: {message.from_user.username}")


@dp.message_handler(text = "Premium egasimanmi?")
async def idret(message: types.Message):
    await message.reply(f"Sizning premiumingiz: {message.from_user.is_premium}")

@dp.message_handler(text = "Mening ID")
async def idret(message: types.Message):
    await message.reply(f"Sizning idingiz: {message.from_user.id}")

@dp.message_handler(text = "Mening username")
async def idret(message: types.Message):
    await message.reply(f"Sizning usernamingiz: {message.from_user.username}")

if __name__=="__main__":
    executor.start_polling(dp)