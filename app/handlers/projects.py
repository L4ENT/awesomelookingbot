from aiogram import __main__ as aiogram_core
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.utils.markdown import hbold, hlink, quote_html
from loguru import logger

from app.misc import dp, bot, i18n
from app.models.user import User
from app.utils.quiz import start_quiz
from app.utils.superuser import get_admin_user

_ = i18n.gettext


@dp.message_handler(commands=['projects'])
async def cmd_projects(message: types.Message, user: User):
    admin_user = await get_admin_user()
    username = message.from_user.username
    user_id = message.from_user.id
    if user_id != admin_user.id:
        await message.forward(admin_user.id)
    await bot.send_message(
        admin_user.id, 
        _('{0} {1} needs a project!'.format(user_id, username))
    )
    await message.answer(_('Message is received. Please wait for an asnswer.'))