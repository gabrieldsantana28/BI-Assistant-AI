from fastapi import APIRouter
from backend.app.services.openai_services import client

router = APIRouter()

@router.get('/chat/test')
def chat_test():
    response = client.responses.create(
        model='gpt-5',
        input='Responda apenas: Olá Gabriel! Sua API está funcionando.'
    )

    return {
        'response': response.output_rext
    }