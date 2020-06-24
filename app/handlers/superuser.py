from aiogram import types

from app.misc import dp, bot, i18n
from app.utils.superuser import create_super_user, get_admin_user

_ = i18n.gettext


@dp.message_handler(commands=["set_superuser"], commands_prefix="!", is_superuser=True)
async def cmd_superuser(message: types.Message):
    args = message.get_args()
    if not args or not args[0].isdigit():
        return False
    args = args.split()
    user_id = int(args[0])
    remove = len(args) == 2 and args[1] == "-rm"

    try:
        result = await create_super_user(user_id=user_id, remove=remove)
    except ValueError:
        result = False

    if result:
        return await message.answer(
            _("Successful changed is_superuser to {is_superuser} for user {user}").format(
                is_superuser=not remove, user=user_id
            )
        )
    return await message.answer(
        _("Failed to set is_superuser to {is_superuser} for user {user}").format(
            is_superuser=not remove, user=user_id
        )
    )

@dp.message_handler(is_superuser=True)
async def admin_messages(message: types.Message):
    rmessage:types.Message = message.reply_to_message
    if rmessage:
        user = rmessage.forward_from
        await bot.send_message(user.id, message.text)
        

@dp.message_handler()
async def admin_messages(message: types.Message):
    admin_user = await get_admin_user()
    if message.from_user.id != admin_user.id:
        await message.forward(admin_user.id)
        
