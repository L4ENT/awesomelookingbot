from aiogram import __main__ as aiogram_core
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
from aiogram.utils.markdown import hbold, hlink, quote_html
from loguru import logger

from app.misc import dp, i18n
from app.models.user import User
from app.utils.keyboard import default_keyboard
from app.utils.quiz import start_quiz
from app.utils.help import get_help
from app.utils.general_info import get_general_information

_ = i18n.gettext


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message, user: User):
    logger.info("User {user} start conversation with bot",
                user=message.from_user.id)

    await message.answer(
        _(
            "(From bot owner) Hello, {user}! Glad to see you here."
            "\n\nThis bot helps me greatly save time and effort on organizational processes. For everything to continue to work like a Swiss watch, I highly recommend using all the features of this bot. Believe me, we will both benefit from it. "
            "\n\nI pass you into his arms )"
        ).format(user=hbold(message.from_user.username)),
        reply_markup=default_keyboard()
    )

    await user.update(start_conversation=True).apply()

    await get_help(message)


@dp.message_handler(Text(equals=_('Help'), ignore_case=True))
@dp.message_handler(Text(equals='Помощь', ignore_case=True))
@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    await get_help(message)


# @dp.message_handler(commands=["version"])
# async def cmd_version(message: types.Message):
#     await message.reply(
#         _("My Engine:\n{aiogram}").format(
#             aiogram=quote_html(str(aiogram_core.SysInfo())))
#     )


@dp.errors_handler()
async def errors_handler(update: types.Update, exception: Exception):
    try:
        raise exception
    except Exception as e:
        logger.exception(
            "Cause exception {e} in update {update}", e=e, update=update)
    return True
