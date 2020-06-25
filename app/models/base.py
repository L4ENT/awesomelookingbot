# Import all the models, so that Base has them before being
# imported by Alembic

from .chat import Chat
from .db import db
from .quiz import Quiz
from .user import User

__all__ = ("db", "Chat", "User")
