from aiogram import Bot, Dispatcher, executor, types

def commands():
    # Токен вашого бота
    API_TOKEN = '7310573884:AAHqe2f5ED23UCGS6GCcDywzHBciZaHE7yI'

    # Ініціалізація бота та диспетчера

    bot = Bot(token=API_TOKEN)

    dp = Dispatcher(bot)
    # Обробник команд
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        print(message.text)
        await message.reply("Привіт! Я бот на базі aiogram.")

    # Обробник текстових повідомлень
    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer(message.text)