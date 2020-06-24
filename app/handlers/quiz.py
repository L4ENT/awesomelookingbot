from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loguru import logger


from app.models.quiz import Quiz
from app.misc import dp, i18n
from app.utils.superuser import get_admin_chat
from app.utils.quiz import QuizQuestions, QuizStates, build_question_text, process_answer

# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
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
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=QuizStates.skills)
@dp.message_handler(state=QuizStates.interests)
@dp.message_handler(state=QuizStates.congestion)
async def process_skills(message: types.Message, state: FSMContext):
    """
    Process question about skills.
    """
    await process_answer(message, state)
