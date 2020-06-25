from aiogram import types

from app.misc import i18n

_ = i18n.gettext


def default_keyboard():
    kb = types.ReplyKeyboardMarkup()
    kb.row(types.KeyboardButton(_("General info")), types.KeyboardButton(_("Get a projects list")))
    kb.add(types.KeyboardButton(_("Start quiz again")))
    kb.row(types.KeyboardButton(_("Settings")), types.KeyboardButton(_("Help")))
    return kb
