from aiogram import types

from bot_app.states import GameStates
from aiogram.dispatcher import FSMContext
from . app import dp , bot
from . keyboards import inline_kb
from . data_fetcher import get_random

@dp.message_handler(commands='train_ten', state='*')
async def train_ten(message: types.Message, state: FSMContext):
    await GameStates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')

        await bot.send_message(message.chat.id, text=f'{data["step"]} из 10\nСлово "{data["word"]}"', reply_markup=inline_kb)

@dp.callback_query_handler(lambda c: c.data in['das','die','der'], state=GameStates.random_ten)
async def button_click_call_back(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data.get('answer'):
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')
            if data['step'] > 10:
                await bot.send_message(callback_query.from_user.id, "Игра закончена\n/train_ten")
                await GameStates.start.set()
            else:
                await bot.send_message(callback_query.from_user.id, 'Да вы угадали\n' + f'{data["step"]} из 10\nСледующее слово "{data["word"]}"', reply_markup=inline_kb)
        else:
            await bot.send_message(callback_query.from_user.id, f'Нет\n', reply_markup=inline_kb)