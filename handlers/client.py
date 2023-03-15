from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client_start, kb_client_categories
# from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
	try:
		await bot.send_message(message.from_user.id,
			'Здравствуйте! Очень мило, что Вы заглянули к нам!\nЧто бы Вы хотели посмотреть?',
			reply_markup=kb_client_start) # kb_client
		await message.delete()
	except:
		await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/BonBonStore_bot")


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 09:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'ул. Колбасная, 15') #, reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
	await sqlite_db.sql_read(message)
	await message.delete()

async def cmd_work_time(message: types.Message):
	await bot.send_message(message.from_user.id, "Мы рады видеть Вас ежедневно\nс 11:00 до 21:00")

async def cmd_address(message: types.Message):
	await bot.send_message(message.from_user.id, "Магазин находится по адресу:\nЛиговский проспект, 171")

async def cmd_goods(message: types.Message):
	# await message.delete()
	# await bot.send_message(message.from_user.id, """Выберите интересующую Вас категорию
	# 	1 - Верхняя одежда
	# 	2 - Платья
	# 	3 - Блузки
	# 	""", reply_markup=types.ReplyKeyboardRemove())
	await message.answer(text="""Выберите интересующую Вас категорию
		1 - Верхняя одежда									 
		2 - Платья
		3 - Блузки
		""", reply_markup=kb_client_categories)

@dp.callback_query_handler(text="button1")
async def press_btn_1(call: types.CallbackQuery):
	await call.message.answer(text="Жмакнул 1й батон")
	await call.answer()

def register_handler_client(dp: Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(pizza_open_command, Text(endswith='работы', ignore_case=True), commands=['Режим_работы'])
	dp.register_message_handler(pizza_place_command, commands=['Расположение'])
	# dp.register_message_handler(pizza_menu_command, Text(equals='меню', ignore_case=True), commands=['Меню'])
	dp.register_message_handler(pizza_menu_command, commands=['Меню'])
	dp.register_message_handler(cmd_work_time, Text(equals='Режим работы'))
	dp.register_message_handler(cmd_address, Text(equals='Адрес'))
	dp.register_message_handler(cmd_goods, Text(equals='Товары'))