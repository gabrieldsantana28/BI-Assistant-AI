from fastapi import APIRouter

from backend.app.schemas.chat import ChatRequest
from backend.app.services.ai_service import ask_ai

router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)

@router.post('/')
def chat(request: ChatRequest):
    resposta = ask_ai(request.message)

    return {
        'response': resposta
    }