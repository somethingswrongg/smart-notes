import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YANDEX_API_KEY")
FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

YANDEX_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"


class AIProviderError(Exception):
    """Ошибка внешнего AI-провайдера"""
    pass

async def summarize_text(text: str) -> str:
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": 1000,
        },
        "messages": [
            {"role": "system", "text": "Кратко резюмируй текст"},
            {"role": "user", "text": text},
        ],
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(YANDEX_URL, headers=headers, json=payload)

    data = response.json()

    if "result" not in data:
        raise Exception(f"YandexGPT error: {data}")

    return data["result"]["alternatives"][0]["message"]["text"]
