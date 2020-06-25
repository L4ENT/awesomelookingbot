from aiogram import types
from aiogram.dispatcher.filters import Text

from app.misc import dp, i18n
from app.utils.general_info import get_general_information
from app.utils.keyboard import default_keyboard

_ = i18n.gettext


@dp.message_handler(Text(equals=_("General info"), ignore_case=True))
@dp.message_handler(Text(equals="Общая информация", ignore_case=True))
@dp.message_handler(commands=["info"])
async def cmd_quiz(message: types.Message):
    """
    Get general information.
    """
    await message.answer(get_general_information())
