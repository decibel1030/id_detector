from aiogram import Dispatcher, Bot, executor, types
from conf import *
import asyncio


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def session_start(message: types.Message):
    await message.answer("A bot that will return the ID of different elements")


@dp.message_handler(commands=["get_id"])
async def get_id(message: types.Message):
    section_end = "\n-----------------------\n"
    if message.reply_to_message:
        text = f"FROM USER ID: <code>{message.reply_to_message.from_user.id}</code>\n" \
               f"FROM USER FN: {message.reply_to_message.from_user.first_name}\n" \
               f"FROM USER LN: {message.reply_to_message.from_user.last_name}" \
               f" {section_end}"
        if message.reply_to_message.forward_from:
            text += f"--FORWARD--\n" \
                    f"isBOT: {message.reply_to_message.forward_from.is_bot}\n" \
                    f"ID: <code>{message.reply_to_message.forward_from.id}</code>\n" \
                    f"FN: {message.reply_to_message.forward_from.first_name}\n" \
                    f"LN: {message.reply_to_message.forward_from.last_name}" \
                    f"{section_end}"
        if message.reply_to_message.document:
            text += f"--DOCUMENT--\n" \
                    f"FILE ID: <code>{message.reply_to_message.document.file_id}</code>\n" \
                    f"UNIQ ID: <code>{message.reply_to_message.document.file_unique_id}</code>"
        if message.reply_to_message.sticker is not None:
            text += f"--STICKER--\n" \
                    f"WIDTH: {message.reply_to_message.sticker.width}\n" \
                    f"HEIGHT: {message.reply_to_message.sticker.height}\n" \
                    f"ANIMATED?: {message.reply_to_message.sticker.is_animated}\n" \
                    f"TARGET EMOJI: {message.reply_to_message.sticker.emoji}\n" \
                    f"FILE ID: <code>{message.reply_to_message.sticker.file_id}\n</code>" \
                    f"UNIQ ID: <code>{message.reply_to_message.sticker.file_unique_id}</code>" \
                    f"{section_end}"

        await message.answer(text=text, parse_mode='html')


if __name__ == '__main__':
    from aiohttp.client_exceptions import ServerDisconnectedError
    from aiogram.utils.exceptions import NetworkError
    while True:
        try:
            executor.start_polling(dp)
        except (ServerDisconnectedError, NetworkError) as ex:
            async def exep():
                print(ex)
                await asyncio.sleep(60*30)
            exep()

