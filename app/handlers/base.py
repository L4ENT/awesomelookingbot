from aiogram import __main__ as aiogram_core
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.utils.markdown import hbold, hlink, quote_html
from loguru import logger

from app.misc import dp, i18n
from app.models.user import User
from app.utils.keyboard import default_keyboard
from app.utils.quiz import start_quiz

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

    await start_quiz(message)


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    logger.info("User {user} read help in {chat}",
                user=message.from_user.id, chat=message.chat.id)
    text = [
        hbold(_("Here you can read the list of my commands:")),
        _("{command} - Start conversation with bot").format(command="/start"),
        _("{command} - Get this message").format(command="/help"),
        _("{command} - Chat or user settings").format(command="/settings"),
        _("{command} - List of avalible projects for you").format(command="/projects"),
        _("{command} - Start the quiz").format(command="/quiz"),
        _("{command} - General info").format(command="/info"),
        hbold(_("You can send any questions with a simple message")),
    ]

    # if types.ChatType.is_private(message):
    #     text.extend(
    #         [
    #             # hbold(_("Available only in PM with bot:")),
    #             # "",
    #             _("In chats this commands list can be other")
    #         ]
    #     )
    # else:
    #     text.extend(
    #         [
    #             hbold(_("Available only in groups:")),
    #             _("{command} - Report message to chat administrators").format(
    #                 command="/report, !report, @admin"
    #             ),
    #             _("{command} - Set RO mode for user").format(command="!ro"),
    #             _("{command} - Ban user").format(command="!ban"),
    #             "",
    #             _("In private chats this commands list can be other"),
    #         ]
    #     )
    await message.reply("\n".join(text), reply_markup=default_keyboard())


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
