from __future__ import annotations

from sqlalchemy.sql import expression

from app.models.db import BaseModel, TimedBaseModel, db
from app.models.user import UserRelatedModel


class Quiz(UserRelatedModel):
    __tablename__ = "quiz"

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    question_text = db.Column(db.String)
    answer_html_text = db.Column(db.String)
