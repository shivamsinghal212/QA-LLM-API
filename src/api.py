from fastapi import APIRouter, UploadFile, File, HTTPException
import json

from fastapi.responses import JSONResponse
from src.utils import get_pdf_text
from src.llm_service import get_llm_chain_obj
from src.schema import Questions, Question

api_routes = APIRouter()


@api_routes.post("/api/qa", response_model=Questions)
async def answer_questions(
    questions_file: UploadFile = File(...), document_file: UploadFile = File(...)
):
    document = None
    response = Questions(questions=[])
    if not questions_file.content_type == "application/json":
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Please upload a JSON questions file.",
        )

    if document_file.content_type not in ["application/pdf", "application/json"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Please upload a JSON/PDF document file.",
        )

    if document_file.content_type == "application/json":
        document = str(await document_file.read())
    if document_file.content_type == "application/pdf":
        document = get_pdf_text(document_file.file.read())
    if document:
        llm_chain = get_llm_chain_obj(documents=document)
        questions_data = json.loads(await questions_file.read())
        all_questions = Questions(questions=questions_data)

        for question in all_questions.questions:
            resp = llm_chain(question.question)
            individual_response = Question(
                question=question.question,
                response=resp["result"],
                id=question.id,
            )
            response.questions.append(individual_response)

    return response
