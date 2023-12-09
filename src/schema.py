from pydantic import BaseModel, validator
from typing import List


class Question(BaseModel):
    id: int
    question: str
    # response: str


class Questions(BaseModel):
    questions: List[Question]

    @validator("questions")
    def ids_must_be_unique(cls, questions):
        if len(questions) != len(set(q.id for q in questions)):
            raise ValueError("Question IDs must be unique")
        return questions
