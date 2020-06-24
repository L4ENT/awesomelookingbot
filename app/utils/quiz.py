from aiogram import types
from aiogram.dispatcher import FSMContext
from loguru import logger

from app.misc import dp, i18n
from app.utils.superuser import create_super_user, get_admin_chat
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.state import State, StatesGroup
from app.models.quiz import Quiz
from app.utils.general_info import get_general_information
from aiogram.utils.markdown import hbold
from app.utils.keyboard import default_keyboard

_ = i18n.gettext


class QuizQuestions:
    """
    Questinons Object
    """

    SKILLS = 'skills'
    INTERESTS = 'interests'
    CONGESTION = 'congestion'

    messages = {
        SKILLS: {
            'question': _('What about your professional skills and experience?'),
            'format': _('You can send a long text with your full story, but surely in single message.'),
            'example': _('I am a website designer. I worked in a digital agency for 2 years. I have very much projects in my suitcase) There is a portfolio [link]. I am often fond a design of fonts ...'),
        },
        INTERESTS: {
            'question': _('What projects and tasks are you interested in (programming, sales, marketing, turnkey projects, short tasks, etc.)?'),
            'format': _('Preferably detailed (thesis), because it will be easier to find the right project for you. Be sure to write in a single message.'),
            'example': _('Turnkey website design, mobile application design, identity, logos'),
        },
        CONGESTION: {
            'question': _('How much time per week are you willing to devote to our joint projects? You can rely on the fact that the average working week is 40 hours.'),
            'format': _('Preferably briefly and necessarily in single message.'),
            'example': _('20 hours a week. Sometimes I work on weekends and holidays'),
        }
    }


THANKU = _('Thanks for answers.')


class QuizStates(StatesGroup):
    """
    Questions sequense.
    """
    skills = State()
    interests = State()
    congestion = State()


def build_question_text(key):
    message_parts = QuizQuestions.messages.get(key)
    question = hbold(_(message_parts.get('question')))
    answer_format = '{0}: {1}'.format(
        hbold(_('Answer format')), _(message_parts.get('format')))
    example = '{0}: {1}'.format(hbold(_('Example')), _(message_parts.get('example')))
    return '\n\n'.join([question, answer_format, example])


async def start_quiz(message: types.Message):
    """
    Starting a quiz.
    """
    logger.info('Quiz: Starting a new quiz')

    # Starting a quiz
    await QuizStates.skills.set()
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton(_('Finish the quiz')))
    await message.answer(
        build_question_text(QuizQuestions.SKILLS), 
        reply_markup=kb
    )


async def process_answer(message: types.Message, state: FSMContext):
    """
    Process question about skills.
    """

    logger.info('Quiz: New skills answer')

    # Fowarding to admin
    chat = await get_admin_chat()
    await message.forward(chat.id)
    current_state: str = await state.get_state()
    _, current_state_name = current_state.split(':')
    # Save message html to db
    await Quiz.create(
        user_id=message.from_user.id,
        question_text=current_state_name,
        answer_html_text=message.html_text
    )

    # Call the next step in quiz
    next_state = await QuizStates.next()

    if next_state:
        _, next_state_name = next_state.split(':')
        # Send a new message
        await message.answer(build_question_text(next_state_name))
    else:
        await state.finish()
        await message.answer(THANKU, reply_markup=default_keyboard())
        await message.answer(get_general_information())
