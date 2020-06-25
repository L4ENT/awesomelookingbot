from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loguru import logger


from app.models.quiz import Quiz
from app.misc import dp, i18n
from app.utils.superuser import get_admin_chat
from app.utils.quiz import QuizQuestions, QuizStates, build_question_text, process_answer, start_quiz
from app.utils.keyboard import default_keyboard

_ = i18n.gettext

@dp.message_handler(Text(equals=_('Start quiz again'), ignore_case=True), state='*')
@dp.message_handler(Text(equals='Заполнить анкету заново', ignore_case=True), state='*')
@dp.message_handler(commands=['quiz'])
async def cmd_quiz(message: types.Message):
    """
    Starting th quiz
    """
    await start_quiz(message)

# You can use state '*' if you need to handle all states


@dp.message_handler(Text(equals=_('Finish the quiz'), ignore_case=True), state='*')
@dp.message_handler(Text(equals='Закончить опрос', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logger.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply(_('The quiz is finished'), reply_markup=default_keyboard())


@dp.message_handler(state=QuizStates.skills)
@dp.message_handler(state=QuizStates.interests)
@dp.message_handler(state=QuizStates.congestion)
async def process_skills(message: types.Message, state: FSMContext):
    """
    Process question about skills.
    """
    await process_answer(message, state)
