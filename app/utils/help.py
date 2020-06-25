from aiogram.utils.markdown import hbold
from app.utils.keyboard import default_keyboard
from app.misc import i18n

_ = i18n.gettext

async def get_help(message):
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

    await message.reply("\n".join(text), reply_markup=default_keyboard())
