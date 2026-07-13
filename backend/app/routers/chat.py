from fastapi import APIRouter
from backend.app.services.ai_service import ask_ai

router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)

@router.get('/test')
def chat_test():
    resposta = ask_ai(
        'Responda apenas: Olá Gabriel! Sua API está funcionando.'
    )

    return {
        'response': resposta
    }