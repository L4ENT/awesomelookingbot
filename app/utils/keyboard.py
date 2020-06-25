from aiogram import types

from app.misc import i18n

_ = i18n.gettext


def default_keyboard():
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton(_('Get a projects list')))
    kb.add(types.KeyboardButton(_('Start quiz again')))
    kb.add(types.KeyboardButton(_('Setting')))
    return kb
