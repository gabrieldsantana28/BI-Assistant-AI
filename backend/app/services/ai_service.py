from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

BASE_DIR = Path(__file__).resolve().parents[3]

PROMPT_PATH = BASE_DIR / 'prompts' / 'system_prompt.txt'

def load_system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")

SYSTEM_PROMPT = load_system_prompt()

def ask_ai(
        prompt: str,
        model: str = 'gpt-5'
) -> str:
    try:
        response = client.responses.create(
            model=model,
            instructions=SYSTEM_PROMPT,
            input=prompt
        )

        return response.output_text
    
    except Exception as e:
        return f'Erro ao consultar a IA: {e}'

