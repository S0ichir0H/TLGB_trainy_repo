from aiogram import types, Dispatcher
import json, string
from create_bot import dp

# фильтр обновляется только при запуске бота
jsload = set(json.load(open('anti_mat.json')))
# @dp.message_handler()


async def echo_send(message: types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(jsload):
		await message.reply('Маты запрещены')
		await message.delete()
	elif message.text.lower() in ["хай", "привет"]:
		await message.answer('И тебе привет!!')
	# await message.reply(message.text)
	# await bot.send_message(message.from_user.id, message.text)


def register_handler_other(dp: Dispatcher):
	dp.register_message_handler(echo_send)

